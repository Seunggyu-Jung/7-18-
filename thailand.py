# if __name__ == "__main__": 을 이용하여 모듈 내에서 직접 실행한 것인지 외부에서 실행한 것인지 판단 가능
class Thailandpackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


#if __name__ == "__main__ ":
#    print("thailand 모듈을 직접 실행")
#    print("이 문장은 모듈을 직접 실행할 때만 실행함")
#    trip_to = Thailandpackage()
#    trip_to.detail()
#else:
#    print("Thailand 외부에서 모듈 호출")