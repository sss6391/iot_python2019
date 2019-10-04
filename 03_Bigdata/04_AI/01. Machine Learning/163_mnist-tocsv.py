import struct
def to_csv(name, maxdata):
    # 레이블 파일과 이미지 파일 열기
    lbl_f = open("./mnist/" + name + "-labels-idx1-ubyte", "rb")
    img_f = open("./mnist/" + name + "-images-idx3-ubyte", "rb")
    csv_f = open("./mnist/" + name + ".csv", "w", encoding="utf-8")
    # 해더 정보 읽기
    # >II big_endian 방식으로 데이터 조회-
    #   데이터를 표현할 때 주소가 큰 값부터 활용한다. 대표프로세서: powerPC,SUN
    # <II little_endian 방식-
    #  주소가 작은 값부터 활용한다. 대표 프로세서: intel
    # read(): 특정 바이트 만큼 데이터를 읽어오는 함수
    # 메타정보를 읽어오는 코드 (메타 정보: 실제 데이터에 대한 정보를 기술하는 부가정보)
    mag1, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag2, img_count = struct.unpack(">II", img_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows * cols
    for idx in range(lbl_count):
        if idx > maxdata: break
        # "B": 숫자를 unsigned char 형식으로 읽기 위한 옵션
        label = struct.unpack("B", lbl_f.read(1))[0]
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label) + ",")
        csv_f.write(",".join(sdata) + "\r\n")
        # 잘 저장 됐는지 이미지 파일로 저장해서 테스트 하기
        if idx < 10:
            # 실제 pgm파일의 메타정보
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
            iname = "./mnist/{0}-{1}-{2}.pgm" .format(name, idx, label)
            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)
    csv_f.close()
    lbl_f.close()
    img_f.close()

# 결과를 파일로 출력하기
# 처음에는 1000개의 데이터로 러신러닝 결과를 본 후 모든 데이터를 활용해보기
# to_csv("train", 1000)
# to_csv("t10k", 500)
#
to_csv("train", 60000)
to_csv("t10k", 10000)
