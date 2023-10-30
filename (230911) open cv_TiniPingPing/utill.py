'''
이미지 데이터가 부족 시 이미지 증폭 클래스 
'''

class ImageAugumentation:
    # filepath : 증폭 시키고 싶은 이미지파일의 경로
    # heigth   : 맞추고 싶은 이미지 높이 == numpy.shape에서의 첫번째 인덱스
    # width    : 맞추고 싶은 이미지 너비 == numpy.shape에서의 두번째 인덱스
    # fixScale : 클래스 생성 시 0이지만 함수 makeUniformsize()를 통해
    #            크기를 고정시킨 데이터 == 이걸로 회전, 반전 등 데이터 증복 시킴
    # augmData : 증폭시킨 데이터를 담아놓는 리스트

    def __init__(self, filepath, height, width):
        import cv2
        self.filepath = filepath
        self.heigth = height
        self.width = width 
        self.fixSclaeImage = 0
        self.augmData = []

    def getAugmentData(self):
        return self.augmData

    def makeUniformSize(self,dsize=None):
        '''
        cv2.resize(src, dsize, fx, fy, interpolation)
        - dsize = (width, height) !! 순서 주의 !!
        - fx, fy : x와 y방향 스케일 비율 -> dsize 값이 (0,0)일 때 유효
            INTER_NEAREST : 최근접 이웃 보간법
            INTER_LINEAR  : 양선형 보간법 (4개 픽셀(2*2) 이용, 효율성 가장 좋음)
            INTER_CUBIC   : 3차회선 보간법 (16개 픽셀(4*4) 이용, linear보다 느리지만 퀄리티 더 좋음
            INTER_LANZOS4 : lanczos 보간법 (64개 픽셀(8*8) 이용, 좀 더 복잡해서 오래 걸리지만 퀄리티는 좋음
            INTER_AREA    : 영상 축소 시 효과적
          => 선택에 따라 클래스에서 수정하기
        '''
        import cv2
        grayIMG = cv2.imread(self.filepath, cv2.IMREAD_GRAYSCALE)

        if dsize == None:
            # 절대적인 크기로 맞춤
            try:
                resizeImage = cv2.resize(src=grayIMG, dsize=(self.width,self.heigth),interpolation=cv2.INTER_LINEAR)
                self.augmData.append(resizeImage)
                self.fixSclaeImage = resizeImage
                return resizeImage
            except:
                print('이미지없음')
                return False
        else:
            # 상대적인 비율로 맞춤(모든 사진을 맞출수 없음) -> 비추천
            try:
                ratio_h = grayIMG.shape[0] / self.heigth
                ratio_w = grayIMG.shape[1] / self.width

                resizeImage = cv2.resize(src=grayIMG, dsize=dsize, fx=ratio_w, fy=ratio_h, interpolation=cv2.INTER_LINEAR)
                self.augmData.append(resizeImage)
                self.fixSclaeImage = resizeImage
                return resizeImage
            except:
                print('이미지없음')
                return False

    def makeFlipData(self,flipDir=[1,0,-1]):
        '''
        이미지 대칭
        cv2.flip(src,flipCode)
        flipCode : 양수 - 좌우 대칭
                   0   - 상하 대칭
                   음수 - 상하좌우 대칭
        '''

        import cv2 

        for dir_ in flipDir:
            dst = cv2.flip(self.fixSclaeImage, dir_)
            self.augmData.append(dst)

    def makeRotateData(self,interval=30, total_degree=360,scale=1):
        '''
        이미지 회전
        (1) 회전 행렬 생성 : cv2.getRotationMatrix2D(center,angle,scale)
                        - center : 기준점(사진의 중앙 or 사진의 꼭지점 .. 사용자 지정 가능 but) 사진의 중앙을 추천)
                        - angle : (반시계 방향) 회전 각도(degree). 음수는 시계방향
                        - scale : 이미지 확대/축소 비율
            => 2*3 회전 행렬 반환 (affine Matrix)
        (2) 회전 : cv2.warpAffine(src, M, dsize)
                        - src : 회전시키고 싶은 이미지 데이터(numpy 형태)
                        - M : affine Matrix(1번에 생성한 행렬)
                        - dsize : 출력 이미지 크기
            => 회전시킨 dsize의 이미지 데이터(numpy 형태)
        :return:
        '''
        import cv2

        center_h = (self.fixSclaeImage.shape[0] // 2) - 1
        center_w = (self.fixSclaeImage.shape[1] // 2) - 1

        # 이미지 중점을 기준으로 30'씩 한바퀴 다 돈다.
        for degree in range(interval, total_degree, interval):
            matrix = cv2.getRotationMatrix2D((center_h, center_w), degree, scale=scale)
            dst1 = cv2.warpAffine(self.fixSclaeImage, matrix, (self.heigth, self.width))
            self.augmData.append(dst1)

    '''
        필터링 : 커널이라고 하는 정방행렬을을 이미지 위 이동 -> 커널과 겹쳐진 이미지 영역과 연산
                    -> 결과값을 이미지 픽셀을 대신하여 새로운 이미지 만든다
                    : 이미지를 구성하는 픽셀들의 조합으로 이미지를 변형하는 방법
                        이미지를 부드럽게 : Blurring
                        선명하게 하는 : Sharpening
    '''
    def makeBlurData(self, endPoint=10):
        '''
        cv2.blur(src, ksize, borderType)
            - src   : 이미지 데이터(numpy)
            - ksize : 평균 필터 크기 (width,height) -> !! 홀수 값 !!
            - borderType : BORDER_REFLECT_101 : 이미지 가장자리 제외한 대칭 방향 인접한 픽셀 값
                           BORDER_CONSTANT : 주어진 특정 값(default:0)으로 채움
                           BORDER_REPLICATE : 가장 가까운 픽셀 값
                           BORDER_REFLECT : 이미지 가장자리 포함한 대칭 방향 인접한 픽셀 값 가져옴
            ==> 필터 내 모든 픽셀에 동일한 가중치를 주어 단순 평균을 한 블러링 기법
                잡음 제거의 전처리 용도로 주로 사용
        cv.GaussianBlur(src, ksize, sigmaX, sigmaY,borderType)
            - sigmaX,sigmaY : 가로(X) 세로(Y)의 표준편차
                              0 입력 시 필터 크기에 의해 자동을 결정 됨
            ==> 필터 중앙에 큰 가중치, 가장자리로 갈수록 작은 가중치
            ==> 원본 이미지의 형상을 좀 더 보존하면서 노이즈 제거
        '''
        import cv2
        for size in range(1, endPoint, 2):
            blurData = cv2.blur(self.fixSclaeImage, (size, size))
            self.augmData.append(blurData)

            gaussianData = cv2.GaussianBlur(self.fixSclaeImage, (size, size), sigmaX=0, sigmaY=0)
            self.augmData.append(gaussianData)

    def makeFilter2D(self):
        '''
        샤프닝(sharpening)
        cv2.filter2D(src, dst, ddepth, kernel,PointAnchor, delta,borderType)
            - dst : 필터가 적용되어 저장될 이미지 변수
            - ddepth : 저장될 이미지의 깊이 : -1(기) / no touch
            - kernel : 이미지에 적용할 필터의 마스크와 연산 정보를 담고 있는 행
            - Point anchor : (-1,-1) / no touch
            - delta : (0,0) / no touch
        '''
        import cv2
        import numpy as np
        kernel = np.array([[0, -1, 0],
                           [-1, 9, -1],
                           [0, -1, 0]])

        filterData = cv2.filter2D(self.fixSclaeImage, -1, kernel)
        self.augmData.append(filterData)
        return filterData

    # 하나의 이미지로 55개의 데이터 만들어 내기
    def createData(self):
        self.makeUniformSize()
        self.makeFlipData()
        self.makeRotateData()
        self.makeBlurData()
        self.makeFilter2D()

    # 이번 티니핑 관련 이미지 과대 펌핑시키기 위해 임의로 만든 함수
    # 사용 비추천
    def integralData(self):
        import numpy as np
        import cv2
        self.fixSclaeImage = self.makeUniformSize()
        center_h = self.fixSclaeImage.shape[0] // 2 - 1
        center_w = self.fixSclaeImage.shape[1] // 2 - 1

        for degree in range(-15, 15, 1): # for degree in range(0, 360, 30):
            matrix = cv2.getRotationMatrix2D((center_h, center_w), degree, 1)
            dst1 = cv2.warpAffine(self.fixSclaeImage, matrix, (self.heigth, self.width))
            for size in range(5, 60, 6):
                gaussianData = cv2.GaussianBlur(dst1, (size, size), sigmaX=0, sigmaY=0)
                self.augmData.append(gaussianData)

    # self.augmData 에 있는 증폭시킨 이미지 데이터(numpy)들을 '.png'데이터로 바꿔서 파일별로 저장 시켜주는 함수
    # 사용자 별로 수정해서 사용하면 됨.
    def createFile(self, dir_, name):
        import os, cv2
        saveDir = dir_ + name.split('_')[0]
        if not os.path.exists(saveDir):
            os.makedirs(saveDir)
        for idx in range(len(self.augmData)):
            cv2.imwrite(saveDir + f'/{name.split(".")[0]}_{idx}.png', self.augmData[idx])