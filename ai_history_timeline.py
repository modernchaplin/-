#!/usr/bin/env python3
"""1950년대부터 현재까지 AI 역사 핵심 키워드를 보여주는 간단한 CLI 프로그램."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AIEvent:
    year: int
    keyword: str
    summary: str


AI_HISTORY: tuple[AIEvent, ...] = (
    AIEvent(1950, "튜링 테스트", "앨런 튜링이 '기계가 생각할 수 있는가?'를 제기하며 AI 철학의 출발점을 제시"),
    AIEvent(1956, "다트머스 회의", "존 매카시가 'Artificial Intelligence' 용어를 제안하며 AI 연구 분야가 공식화"),
    AIEvent(1958, "퍼셉트론", "프랭크 로젠블랫이 초기 신경망 모델 퍼셉트론을 발표"),
    AIEvent(1966, "ELIZA", "자연어 대화 프로그램 ELIZA가 등장해 초기 챗봇 가능성을 보여줌"),
    AIEvent(1974, "1차 AI 겨울", "기대 대비 성과 부족과 예산 축소로 AI 연구가 침체"),
    AIEvent(1980, "전문가 시스템 붐", "규칙 기반 전문가 시스템이 산업 현장에서 상용화되기 시작"),
    AIEvent(1987, "2차 AI 겨울", "전문가 시스템 한계와 유지비용 문제로 다시 투자 위축"),
    AIEvent(1997, "딥블루", "IBM 딥블루가 체스 챔피언 가리 카스파로프를 이김"),
    AIEvent(2006, "딥러닝 재부상", "제프리 힌턴 등이 심층신경망 학습 기법을 재조명"),
    AIEvent(2012, "AlexNet", "이미지넷 대회에서 딥러닝이 압도적 성능을 기록하며 전환점 형성"),
    AIEvent(2016, "알파고", "구글 딥마인드 알파고가 이세돌을 이기며 강화학습 가능성 입증"),
    AIEvent(2017, "트랜스포머", "논문 'Attention Is All You Need'로 현대 생성형 AI의 기반 확립"),
    AIEvent(2020, "대규모 언어모델", "GPT-3 등 거대 모델이 자연어 생성의 품질을 크게 향상"),
    AIEvent(2022, "생성형 AI 대중화", "ChatGPT 공개를 계기로 일반 사용자 중심 AI 활용이 폭발적으로 확대"),
    AIEvent(2024, "멀티모달·에이전트", "텍스트·이미지·음성 통합 모델과 작업 자동화 AI 에이전트가 확산"),
)


def filter_by_year(events: Iterable[AIEvent], start: int, end: int) -> list[AIEvent]:
    """연도 범위에 맞는 이벤트 목록을 반환한다."""
    return [event for event in events if start <= event.year <= end]


def print_timeline(events: Iterable[AIEvent]) -> None:
    print("\n=== AI 역사 핵심 타임라인 ===")
    for event in events:
        print(f"{event.year} | {event.keyword}\n  - {event.summary}")


def top_keywords(events: Iterable[AIEvent], limit: int = 10) -> list[str]:
    """핵심 키워드를 앞에서부터 limit개 반환한다."""
    return [event.keyword for event in list(events)[:limit]]


def main() -> None:
    print("AI 역사 프로그램 (1950s ~ 현재)")
    print("원하는 연도 범위를 입력하면 핵심 사건과 키워드를 보여줍니다.\n")

    try:
        start = int(input("시작 연도 (예: 1950): ").strip() or "1950")
        end = int(input("종료 연도 (예: 2025): ").strip() or "2025")
    except ValueError:
        print("숫자로 된 연도를 입력해 주세요.")
        return

    if start > end:
        print("시작 연도는 종료 연도보다 클 수 없습니다.")
        return

    selected = filter_by_year(AI_HISTORY, start, end)
    if not selected:
        print("선택한 범위에 해당하는 데이터가 없습니다.")
        return

    print_timeline(selected)

    print("\n=== 이 범위의 핵심 키워드 ===")
    print(", ".join(top_keywords(selected, limit=12)))


if __name__ == "__main__":
    main()
