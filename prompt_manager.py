"""나만의 프롬프트 관리 프로그램 (콘솔 기반)."""

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": (
            "당신은 10년 경력의 전문 블로거입니다.\n"
            "주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.\n"
            "서론, 본론, 결론 구조를 갖추고,\n"
            "독자의 관심을 끄는 제목을 3개 제안해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": True,
    },
    {
        "title": "제품 썸네일 생성",
        "content": (
            "다음 제품의 매력적인 썸네일 이미지를 생성해주세요.\n"
            "밝은 스튜디오 조명, 깔끔한 단색 배경, 제품이 중앙에 크게 보이는 구도,\n"
            "고해상도 16:9 비율."
        ),
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "광고 스크립트 작성",
        "content": (
            "15초 분량의 제품 광고 영상 스크립트를 작성해주세요.\n"
            "장면 구성(컷 번호), 내레이션, 자막 문구를 표 형태로 정리해주세요."
        ),
        "category": "영상 생성",
        "favorite": False,
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": (
            "당신은 15년 경력의 IT 컨설턴트입니다.\n"
            "비전문가도 이해할 수 있는 쉬운 언어로 설명하고,\n"
            "항상 장단점과 비용 관점을 함께 제시해주세요."
        ),
        "category": "페르소나",
        "favorite": False,
    },
    {
        "title": "뉴스 요약 프롬프트",
        "content": (
            "아래 뉴스 기사를 3줄로 요약하고, 핵심 키워드 5개를 추출해주세요.\n"
            "마지막에 이 뉴스가 업무에 미칠 영향을 한 문장으로 덧붙여주세요."
        ),
        "category": "자동화",
        "favorite": False,
    },
]


def read_nonempty(label):
    """빈 입력이 아닐 때까지 반복해서 입력을 받는다."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("입력값이 비어 있습니다. 다시 입력해주세요.")


def read_int(label):
    """정수가 입력될 때까지 반복한다. 변환 실패 시 None을 반환한다."""
    try:
        return int(input(label).strip())
    except ValueError:
        return None


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def main():
    handlers = {}  # 이후 커밋에서 기능이 추가될 때마다 채워진다
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        handler = handlers.get(choice)
        if handler is None:
            print("잘못된 입력입니다. 메뉴에 있는 번호를 입력해주세요.")
            continue
        handler()


if __name__ == "__main__":
    main()
