---
title: "바이낸스 탈취(2026) 두 모델 코딩 대조 시트"
type: sheet
status: draft
created: 2026-11-13
updated: 2026-11-13
---

# 바이낸스 탈취(2026) 두 모델 코딩 대조 시트

## 집계

- 비교 필드 44(템플릿 펼친 항목 45 − `annotation_pass`). 그 가운데 `techniques`는 코딩 대상 아님.
- **일치 28 · 서술 차이 10 · 값 불일치 3 · 한쪽 결측 2 · 코딩 대상 아님 1**
- 일치 28 가운데 코딩하지 않은 칸 8(템플릿 선기입 6 — `case_id` · `tier` · `victim_state` · `collection_mode` · `collection_mode_basis` · `identified_date` / 두 코더 모두 빈 메타 키 2 — `terminal_objective` · `countermeasure_availability`). 독립 코딩 값이 일치한 칸은 **20**이다.
- 일치가 아닌 필드: `c_id.basis`(서술 차이) · `c_st.basis`(서술 차이) · `access_depth.basis`(서술 차이) · `effect_realized.note`(서술 차이) · `effect_realized.time_basis`(서술 차이) · `intrusion_state.basis`(서술 차이) · `legal_characterization`(값 불일치) · `responses`(값 불일치) · `aftermath`(한쪽 결측) · `boundary_flag`(값 불일치) · `boundary_reason`(한쪽 결측) · `notes`(서술 차이) · `target_specificity_basis`(서술 차이) · `victim_sector_sub_note`(서술 차이) · `victim_assets`(서술 차이)

## 머리 안내

> 묶음 `pack/` 25건(수집자 메모 가림 사본)을 Claude Opus(코더 A)와 Claude Fable(코더 B)이 서로의 산출을 보지 않고 격리 디렉터리에서 독립 코딩했다(지시문 `issued/coding_instructions_binance.md`). 이 시트는 두 산출을 기계로 견준 것이다. 어느 값이 맞는지 고르지 않는다. 「저자 확정」 칸은 저자가 채운다.
> 이 시트는 보조 스크립트가 만든다(생성 시각을 적지 않는다 — 같은 입력이면 다시 만들어도 바이트가 같다).
> 입력 sha256(수거한 사본 `coding/<모델>/`): `coding_claude_opus.json` `f601f864dc57b656244bf28d0d35d59316b9f9a54e63af634c7b7c9e14754d3e` (배정 값과 같음) · `coding_claude_opus_근거.md` `839241f4f969788f8359110456123f182cbff5d2b6254baf267584880f3753a4` (배정 값과 같음) · `coding_claude_fable.json` `de81d7422d422f9e82c857efff4f805cda224131605893d0bf1c7838a6cb0632` (배정 값과 같음) · `coding_claude_fable_근거.md` `385a7b576efda20301091afc0cebcfb4eb9116d2cc10b11f931da8d303889023` (배정 값과 같음).
> 줄 끝: 네 파일 모두 LF(CR LF 없음) — 정규화하지 않았다.
> **기계 검사**(아래 「기계 검사」 절): 키 구성 · 선기입 값 · 근거 구절 원문 대조 · 인용 금지 구간 · 원문 열람 증명. 정식 검증자 보고가 아니라 이 시트를 만들며 한 기계 대조다.
> **머리 사실**: 코더 모델(세션 기록의 응답 모델) — A `claude-opus-5-5` · B `claude-fable-5-2` · 격리 사본 목록 해시 `81f64236…` · 묶음 25건.
> **치환**: 없음(`c_st.reference_date`의 「공식 성명 없음」 토큰은 두 코더 모두 쓰지 않았다 — 치환 대상 0).
> **줄 보완**(값 안 「 」 인용에 파일:줄 없음 · 부록 A): A(Opus) 1곳 · B(Fable) 0곳.
> **저자 확정 기입**(2026-11-13): 저자 결정(일치한 나머지 값은 그대로)을 전달받아 그 선택만 칸에 옮겼다(새 값 없음 · 에이전트 후보·추천 없음). 칸의 말: 「두 코더 일치 · 그대로」 · 「코더 A의 값」 · 「코더 A의 문면」 · 「코딩 대상 아님」. 확정 기록 `author_confirmation_binance.json` · 확정 레코드 `../입력레코드_binance_확정.jsonl`.

## 기계 검사

| 검사 | 코더 A(Opus) | 코더 B(Fable) |
|---|---|---|
| (가) 키 34개 · 순서 · 하위 키 | 통과 | 통과 |
| (라) 선기입 값(`victim_state` · `identified_date` · `collection_mode` · `techniques` + `case_id` · `tier` · `collection_mode_basis` · `terminal_objective` · `countermeasure_availability` · `annotation_pass`) | 통과 | 통과 |
| (나) 근거 구절 원문 대조(§1 표 + JSON 값 · 근거 md 본문의 「구절」(파일:줄) · `legal_characterization` · `victim_assets`) | 일치 157 | 일치 132 |
| (다) 인용 금지 구간(`tech_` 1~4행 · `resp_16` 1~2행 · `resp_17` · `resp_18` 1행 · `tech_10` 403~442행)을 파일:줄로 든 곳 | 인용 0건 | 인용 0건 |
| §0 원문 열람 증명(적힌 sha256 = 사본 바이트 = `manifest_min.json` · 읽은 범위) | 25행 · 해시 불일치 0 · 읽은 범위가 전 줄을 덮지 않음 0 | 25행 · 해시 불일치 0 · 읽은 범위가 전 줄을 덮지 않음 0 |

- 대조 방식: 파일:줄이 가리키는 줄(범위면 이어 붙인 줄)에 구절이 글자 그대로 들어 있으면 「일치」, 공백만 다르면 「공백만 다름」. 같은 구절 · 같은 파일:줄은 한 번만 센다. 「묶음에 근거 없음」 행은 세지 않는다.

## 1. 필드별 대조 — 44필드(템플릿 순서 · 「저자 확정」은 저자가 채운다)

> 값 칸은 앞부분만(전체 값은 부록 B). 근거 칸 = 근거 md §1의 행 수 · 첫 행의 근거 md 줄 · 파일:줄 · 첫 구절 앞부분.

| # | 필드 | 코더 A(Opus) 값과 근거 구절 | 코더 B(Fable) 값과 근거 구절 | 일치 여부 | 저자 확정 |
|---|---|---|---|---|---|
| 1 | `case_id` | BINANCE-2026<br>근거: — (메타 키 · 행 불요) | BINANCE-2026<br>근거: — (메타 키 · 행 불요) | 일치 | 두 코더 일치 · 템플릿 값 그대로 |
| 2 | `name` (자유 서술) | 바이낸스 탈취 사건(2026)<br>근거: 1행 · 근거.md:37 · tech_04_FBI_20261031.txt:8 · 「The Federal Bureau of Investigation (FBI) is releasing information adv…」 | 바이낸스 탈취 사건(2026)<br>근거: 1행 · 근거.md:37 · tech_04_FBI_20261031.txt:8 · 「The Federal Bureau of Investigation (FBI) is releasing information adv…」 | 일치 | 두 코더 일치 · 그대로 |
| 3 | `alias` | Jade Sleet, UNC4899, Slow Pisces, Pressure Chollima<br>근거: 1행 · 근거.md:38 · tech_13_ReversingLabs_20261031.txt:142 · 「TraderTraitor, also tracked as Jade Sleet, UNC4899, Slow Pisces and Pr…」 | Jade Sleet, UNC4899, Slow Pisces, Pressure Chollima<br>근거: 1행 · 근거.md:38 · tech_13_ReversingLabs_20261031.txt:142 · 「TraderTraitor, also tracked as Jade Sleet, UNC4899, Slow Pisces and Pr…」 | 일치 | 두 코더 일치 · 그대로 |
| 4 | `actor` | TraderTraitor<br>근거: 2행 · 근거.md:39 · tech_04_FBI_20261031.txt:8 · resp_16_DOJ_20261112.txt:30 · 「The FBI refers to this specific North Korean malicious cyber activity …」 | TraderTraitor<br>근거: 1행 · 근거.md:39 · tech_04_FBI_20261031.txt:8 · 「The FBI refers to this specific North Korean malicious cyber activity …」 | 일치 | 두 코더 일치 · 그대로 |
| 5 | `c_id.grade` | 5<br>근거: 2행 · 근거.md:41 · tech_04_FBI_20261031.txt:8 · resp_16_DOJ_20261112.txt:30 · 「The FBI refers to this specific North Korean malicious cyber activity …」 | 5<br>근거: 4행 · 근거.md:40 · tech_04_FBI_20261031.txt:8 · resp_16_DOJ_20261112.txt:30 · tech_05_TRMLabs_20261029.txt:14 · tech_08_Chainalysis_20261030.txt:20 · 「The Federal Bureau of Investigation (FBI) is releasing information adv…」 | 일치 | 두 코더 일치 · 그대로 |
| 6 | `c_id.basis` (자유 서술) | 식별 시점(2026-11-12) 등급 5 — 정부 문서가 이 작전을 단정 서술어로 TraderTraitor의 것으로 지목: FBI(2026-10-31) 「The FBI refers to this s…<br>근거: 3행 · 근거.md:43 · tech_05_TRMLabs_20261029.txt:14 · tech_08_Chainalysis_20261030.txt:20 · tech_07_Elliptic_20261030.txt:24 · 「TRM attributes the attack to TraderTraitor, North Korea’s elite hackin…」 | 식별 시점(2026-11-12) 기준 등급. 2026-10-31 FBI 경보가 수행 주체를 단정 서술 — 「The Federal Bureau of Investigation (FBI) is relea…<br>근거: 1행 · 근거.md:44 · tech_04_FBI_20261031.txt:8 · 「The FBI refers to this specific North Korean malicious cyber activity …」 | 서술 차이 | 코더 A의 문면 |
| 7 | `c_id.source` | tech_04_FBI_20261031.txt; resp_16_DOJ_20261112.txt<br>근거: — (메타 키 · 행 불요) | tech_04_FBI_20261031.txt; resp_16_DOJ_20261112.txt<br>근거: — (메타 키 · 행 불요) | 일치 | 두 코더 일치 · 그대로 |
| 8 | `state_attribution` | 북한<br>근거: 2행 · 근거.md:46 · tech_04_FBI_20261031.txt:8 · resp_16_DOJ_20261112.txt:30 · 「The Federal Bureau of Investigation (FBI) is releasing information adv…」 | 북한<br>근거: 2행 · 근거.md:45 · tech_04_FBI_20261031.txt:8 · resp_16_DOJ_20261112.txt:15 · 「the Democratic People's Republic of Korea (North Korea) was responsibl…」 | 일치 | 두 코더 일치 · 그대로 |
| 9 | `c_st.grade` | 5<br>근거: 1행 · 근거.md:48 · resp_16_DOJ_20261112.txt:30 · 「members of the North Korean military, referred to by the FBI as “Trade…」 | 5<br>근거: 2행 · 근거.md:47 · resp_16_DOJ_20261112.txt:30 · resp_16_DOJ_20261112.txt:15 · 「members of the North Korean military, referred to by the FBI as “Trade…」 | 일치 | 두 코더 일치 · 그대로 |
| 10 | `c_st.basis` (자유 서술) | 식별 시점(2026-11-12) 기준 등급 5(국가기관 소속 특정) — 미 법무부 보도자료(2026-11-12)가 수행자를 북한 군 소속으로 특정: 「members of the North Korea…<br>근거: 2행 · 근거.md:53 · tech_13_ReversingLabs_20261031.txt:110 · tech_17_Rekt_20261106.txt:425 · 「North Korea has denied involvement.」 | 식별 시점(2026-11-12) 기준 등급. 2026-11-12 미 법무부 보도자료가 수행자를 국가기관(군) 소속으로 특정 — 「members of the North Korean military, …<br>근거: 1행 · 근거.md:49 · resp_16_DOJ_20261112.txt:30 · 「members of the North Korean military, referred to by the FBI as “Trade…」 | 서술 차이 | 코더 A의 문면 |
| 11 | `c_st.source` | resp_16_DOJ_20261112.txt; tech_04_FBI_20261031.txt<br>근거: — (메타 키 · 행 불요) | resp_16_DOJ_20261112.txt; tech_04_FBI_20261031.txt<br>근거: — (메타 키 · 행 불요) | 일치 | 두 코더 일치 · 그대로 |
| 12 | `c_st.reference_date` | 2026-11-12<br>근거: 2행 · 근거.md:49 · resp_16_DOJ_20261112.txt:6 · resp_16_DOJ_20261112.txt:30 · 「Thursday, November 12, 2026」 | 2026-11-12<br>근거: 2행 · 근거.md:50 · resp_16_DOJ_20261112.txt:30 · resp_16_DOJ_20261112.txt:6 · 「members of the North Korean military, referred to by the FBI as “Trade…」 | 일치 | 두 코더 일치 · 그대로 |
| 13 | `victim_sector` | finance_commerce<br>근거: 1행 · 근거.md:55 · tech_04_FBI_20261031.txt:8 · 「cryptocurrency exchange Binance」 | finance_commerce<br>근거: 1행 · 근거.md:55 · resp_16_DOJ_20261112.txt:15 · 「Binance, a virtual currency exchange」 | 일치 | 두 코더 일치 · 그대로 |
| 14 | `victim_state` | 미국<br>근거: — (메타 키 · 행 불요) | 미국<br>근거: — (메타 키 · 행 불요) | 일치 | 두 코더 일치 · 템플릿 선기입 값 그대로(작업 규칙) |
| 15 | `techniques` | []<br>근거: — (메타 키 · 행 불요) | []<br>근거: — (메타 키 · 행 불요) | 코딩 대상 아님 | 코딩 대상 아님 · 빈 목록 그대로(추출기가 채운다 · 작업 규칙) |
| 16 | `terminal_objective` | {}<br>근거: — (메타 키 · 행 불요) | {}<br>근거: — (메타 키 · 행 불요) | 일치 | 두 코더 일치 · 비우는 메타 키 그대로 |
| 17 | `access_depth.draft` | core<br>근거: 2행 · 근거.md:59 · tech_01_Binance_20261103.txt:27 · tech_01_Binance_20261103.txt:83 · 「The attacker exploited unauthorized access to an internal wallet signi…」 | core<br>근거: 2행 · 근거.md:56 · tech_01_Binance_20261103.txt:27 · tech_01_Binance_20261103.txt:83 · 「The attacker exploited unauthorized access to an internal wallet signi…」 | 일치 | 두 코더 일치 · 그대로 |
| 18 | `access_depth.basis` (자유 서술) | 한 침투 안의 최댓값 = 내부 지갑 서명 서비스(특권 자산) 도달: 「The attacker exploited unauthorized access to an internal wallet signin…<br>근거: 1행 · 근거.md:61 · tech_11_Hacken_20261030.txt:24 · 「the attacker used a stolen token to deploy a container that sent unaut…」 | 한 침투 안의 최댓값(관측 서술만). 2026-09 엔지니어 B의 업무용 컴퓨터 감염 「Engineer B was instructed to download an “assignment” contain…<br>근거: 1행 · 근거.md:58 · tech_01_Binance_20261103.txt:27 · 「The attacker exploited unauthorized access to an internal wallet signi…」 | 서술 차이 | 코더 A의 문면 |
| 19 | `timing_grade` | 절대(사건 수준)<br>근거: 2행 · 근거.md:62 · tech_01_Binance_20261103.txt:29 · tech_01_Binance_20261103.txt:47 · 「Between 20:05 UTC and 20:09 UTC, five Binance hot wallets sent 233.46 …」 | 절대(사건 수준)<br>근거: 2행 · 근거.md:59 · tech_01_Binance_20261103.txt:29 · tech_01_Binance_20261103.txt:83 · 「Between 20:05 UTC and 20:09 UTC, five Binance hot wallets sent 233.46 …」 | 일치 | 두 코더 일치 · 그대로 |
| 20 | `effect_realized.value` | post<br>근거: 1행 · 근거.md:64 · tech_01_Binance_20261103.txt:13 · 「Approximately USD 6.34 billion in digital assets were impacted by the …」 | post<br>근거: 1행 · 근거.md:61 · tech_01_Binance_20261103.txt:13 · 「Approximately USD 6.34 billion in digital assets were impacted by the …」 | 일치 | 두 코더 일치 · 그대로 |
| 21 | `effect_realized.by_type` | {"1": "post", "2": "post", "3": "pre"}<br>근거: 7행 · 근거.md:65 · tech_01_Binance_20261103.txt:83 · tech_01_Binance_20261103.txt:55 · tech_01_Binance_20261103.txt:41 · tech_01_Binance_20261103.txt:27 · tech_04_FBI_20261031.txt:8 외 2 · 「used the credentials stolen from Wallet DevOps Engineer A」 | {"1": "post", "2": "post", "3": "pre"}<br>근거: 7행 · 근거.md:62 · tech_01_Binance_20261103.txt:83 · tech_01_Binance_20261103.txt:55 · tech_01_Binance_20261103.txt:29 · tech_01_Binance_20261103.txt:47 · tech_04_FBI_20261031.txt:8 외 2 · 「used the credentials stolen from Wallet DevOps Engineer A」 | 일치 | 두 코더 일치 · 그대로 |
| 22 | `effect_realized.boundary_flag` | true<br>근거: 1행 · 근거.md:72 · tech_01_Binance_20261103.txt:9 · 「we apologise for the concern, disruption and uncertainty it caused our…」 | true<br>근거: 2행 · 근거.md:69 · tech_01_Binance_20261103.txt:9 · tech_07_Elliptic_20261030.txt:14 · 「This should not have happened, and we apologise for the concern, disru…」 | 일치 | 두 코더 일치 · 그대로 |
| 23 | `effect_realized.note` (자유 서술) | 유형 ②: 자산 탈취는 지시문 §3-3에 따라 유형 ②(조작·공개) 칸에서 판정 — 「The attackers submitted 50 signing transactions …<br>근거: 1행 · 근거.md:73 · tech_01_Binance_20261103.txt:41 · 「The attackers submitted 50 signing transactions to manipulate the acco…」 | 유형 ②(조작·공개): 지시문 §3-3에 따라 자산 탈취를 이 칸에서 판정 — 2026-10-29 20:05~23:56 UTC 핫월렛 자산이 공격자 주소로 이전 「Between 20:05 UTC a…<br>근거: 1행 · 근거.md:71 · tech_01_Binance_20261103.txt:39 · 「Binance immediately initiated multiple containment measures, including…」 | 서술 차이 | 코더 A의 문면 |
| 24 | `effect_realized.time_basis` (자유 서술) | 식별 시점 2026-11-12 기준(효과 발현: 자산 이동 2026-10-29 20:05~23:56 UTC — tech_01_Binance_20261103.txt:29 · tech_01_Binanc…<br>근거: 1행 · 근거.md:74 · tech_01_Binance_20261103.txt:29 · 「Between 20:05 UTC and 20:09 UTC, five Binance hot wallets sent 233.46 …」 | 식별 시점 2026-11-12 기준<br>근거: 1행 · 근거.md:72 · resp_16_DOJ_20261112.txt:6 · 「Thursday, November 12, 2026」 | 서술 차이 | 코더 A의 문면 |
| 25 | `intrusion_state.value` | terminated<br>근거: 3행 · 근거.md:75 · tech_01_Binance_20261103.txt:15 · tech_01_Binance_20261103.txt:47 · tech_01_Binance_20261103.txt:49 · 「The entry points identified as having been used in the attack have bee…」 | terminated<br>근거: 6행 · 근거.md:73 · tech_01_Binance_20261103.txt:15 · tech_01_Binance_20261103.txt:47 · tech_01_Binance_20261103.txt:49 · tech_01_Binance_20261103.txt:95 · tech_01_Binance_20261103.txt:17 외 1 · 「The entry points identified as having been used in the attack have bee…」 | 일치 | 두 코더 일치 · 그대로 |
| 26 | `intrusion_state.basis` (자유 서술) | 식별 시점(2026-11-12)에 존속하는 무단 접근 서술 없음 — 2026-11-03 보고 기준 진입점 폐쇄·경로 시스템 재구축: 「The entry points identified as havi…<br>근거: 1행 · 근거.md:78 · tech_01_Binance_20261103.txt:17 · 「The investigation remains ongoing」 | 식별 시점(2026-11-12) 기준. 2026-10-29 23:56 UTC 마지막 무단 이체 뒤 추가 무단 이체 없음 「No further unauthorised transfers were obs…<br>근거: 1행 · 근거.md:79 · tech_01_Binance_20261103.txt:15 · 「The entry points identified as having been used in the attack have bee…」 | 서술 차이 | 코더 A의 문면 |
| 27 | `countermeasure_availability` | <br>근거: — (메타 키 · 행 불요) | <br>근거: — (메타 키 · 행 불요) | 일치 | 두 코더 일치 · 비우는 메타 키 그대로 |
| 28 | `conflict_nexus` | none<br>근거: 4행 · 근거.md:79 · manifest_min.json(묶음 25건 전체) · 묶음에 근거 없음 | none<br>근거: 4행 · 근거.md:80 · — · 묶음에 근거 없음 | 일치 | 두 코더 일치 · 그대로 |
| 29 | `legal_characterization` | [{"value": "domestic_political_framing", "quote": "identifying, mitigating, and disrupting North Korea's illic…<br>근거: 2행 · 근거.md:83 · tech_04_FBI_20261031.txt:18 · resp_16_DOJ_20261112.txt:19 · 「identifying, mitigating, and disrupting North Korea's illicit cybercri…」 | [{"value": "domestic_political_framing", "quote": "The FBI refers to this specific North Korean malicious cybe…<br>근거: 4행 · 근거.md:84 · tech_04_FBI_20261031.txt:8 · resp_17_외교부_20261105.txt:26 · resp_16_DOJ_20261112.txt:16 · resp_16_DOJ_20261112.txt:19 · 「The FBI refers to this specific North Korean malicious cyber activity …」 | 값 불일치 — 항목 A 2 · B 4 | 코더 A의 값 |
| 30 | `responses` | [{"type": "public_attribution", "actor_state": "미국", "date": "2026-10-31", "invoked_legal_basis": "none_stated…<br>근거: 10행 · 근거.md:85 · tech_04_FBI_20261031.txt:8 · tech_13_ReversingLabs_20261031.txt:110 · tech_17_Rekt_20261106.txt:423 · tech_04_FBI_20261031.txt:10 · tech_04_FBI_20261031.txt:14 외 3 · 「The Federal Bureau of Investigation (FBI) is releasing information adv…」 | [{"type": "public_attribution", "actor_state": "미국", "date": "2026-10-31", "invoked_legal_basis": "none_stated…<br>근거: 9행 · 근거.md:88 · tech_04_FBI_20261031.txt:8 · tech_13_ReversingLabs_20261031.txt:110 · tech_07_Elliptic_20261030.txt:16 · resp_16_DOJ_20261112.txt:30 · resp_16_DOJ_20261112.txt:6 외 2 · 「The Federal Bureau of Investigation (FBI) is releasing information adv…」 | 값 불일치 — 항목 A 4 · B 3 · 공통 구조 3 | 코더 A의 값 4항목 |
| 31 | `aftermath` (자유 서술) | 식별 시점(2026-11-12) 이후의 후속: 묶음에 근거 없음(자료 기준일도 2026-11-12). 식별 시점에 진행 중으로 적힌 것 — 미 법무부(2026-11-12) 「Efforts to tr…<br>근거: 3행 · 근거.md:95 · resp_16_DOJ_20261112.txt:31 · resp_18_외교부_20261110.txt:19 · 묶음에 근거 없음 | <br>근거: 1행 · 근거.md:97 · — · 묶음에 근거 없음 | 한쪽 결측 — B 비어 있음 | 코더 A의 값 |
| 32 | `tier` | v3_case<br>근거: — (메타 키 · 행 불요) | v3_case<br>근거: — (메타 키 · 행 불요) | 일치 | 두 코더 일치 · 템플릿 값 그대로 |
| 33 | `boundary_flag` | true<br>근거: 1행 · 근거.md:98 · tech_04_FBI_20261031.txt:8 · 「The Federal Bureau of Investigation (FBI) is releasing information adv…」 | false<br>근거: 1행 · 근거.md:98 · — · 묶음에 근거 없음 | 값 불일치 | 코더 A의 값 |
| 34 | `boundary_reason` (자유 서술) | 효과 유형 경계 — 묶음은 이 사건을 'theft'(tech_04_FBI_20261031.txt:8)로 서술하나 저자 결정에 따라 자산 탈취를 유형 ②(조작·공개)로 판정했다(유형 ①…<br>근거: 1행 · 근거.md:99 · tech_01_Binance_20261103.txt:9 · 「we apologise for the concern, disruption and uncertainty it caused our…」 | <br>근거: 1행 · 근거.md:99 · — · 묶음에 근거 없음 | 한쪽 결측 — B 비어 있음 | 코더 A의 값 |
| 35 | `notes` (자유 서술) | ⑴ 금전 동기(판정에 쓰지 않음): 「This group has repeatedly targeted the cryptocurrency industry, exchanges, DeFi protocols…<br>근거: 8행 · 근거.md:100 · tech_08_Chainalysis_20261030.txt:30 · resp_16_DOJ_20261112.txt:16 · tech_10_Cointegrity_20261030.txt:230 · tech_17_Rekt_20261106.txt:425 · tech_13_ReversingLabs_20261031.txt:142 외 3 · 「This group has repeatedly targeted the cryptocurrency industry, exchan…」 | [금전 동기] 묶음은 탈취 목적을 정권 자금 조달로 서술 — 「This group has repeatedly targeted the cryptocurrency industry, exchanges, …<br>근거: 1행 · 근거.md:100 · tech_08_Chainalysis_20261030.txt:30 · 「This group has repeatedly targeted the cryptocurrency industry, exchan…」 | 서술 차이 | 코더 A의 문면 |
| 36 | `unit_type` | campaign<br>근거: 1행 · 근거.md:108 · tech_01_Binance_20261103.txt:53 · 「Our current investigation indicates that this was a sophisticated, mul…」 | campaign<br>근거: 1행 · 근거.md:101 · tech_01_Binance_20261103.txt:53 · 「Our current investigation indicates that this was a sophisticated, mul…」 | 일치 | 두 코더 일치 · 그대로 |
| 37 | `collection_mode` | organic<br>근거: — (메타 키 · 행 불요) | organic<br>근거: — (메타 키 · 행 불요) | 일치 | 두 코더 일치 · 템플릿 선기입 값 그대로(작업 규칙) |
| 38 | `collection_mode_basis` (자유 서술) | 저자가 사례로 선정(2026-11-13), 표적 수집 아님<br>근거: — (메타 키 · 행 불요) | 저자가 사례로 선정(2026-11-13), 표적 수집 아님<br>근거: — (메타 키 · 행 불요) | 일치 | 두 코더 일치 · 템플릿 선기입 문구 그대로(작업 규칙) |
| 39 | `target_specificity` | specific_victim<br>근거: 1행 · 근거.md:109 · tech_01_Binance_20261103.txt:59 · 「Software Engineer B had a profile on the platform that referenced his …」 | specific_victim<br>근거: 3행 · 근거.md:102 · tech_01_Binance_20261103.txt:59 · tech_04_FBI_20261031.txt:8 · tech_01_Binance_20261103.txt:55 · 「Software Engineer B had a profile on the platform that referenced his …」 | 일치 | 두 코더 일치 · 그대로 |
| 40 | `target_specificity_basis` (자유 서술) | 바이낸스와 그 지갑 인프라 담당자를 특정해 겨냥: 「Software Engineer B had a profile on the platform that referenced his experience …<br>근거: 1행 · 근거.md:110 · tech_01_Binance_20261103.txt:55 · 「However, Engineer A’s role and his related colleagues on our wallet in…」 | 특정 기관(바이낸스)의 지갑 인프라 담당자를 겨냥한 침투 — 2026-06 지갑 DevOps 엔지니어 A의 역할·동료 노출 「However, Engineer A’s role and his relat…<br>근거: 1행 · 근거.md:105 · tech_01_Binance_20261103.txt:59 · 「Software Engineer B had a profile on the platform that referenced his …」 | 서술 차이 | 코더 A의 문면 |
| 41 | `victim_sector_sub` | financial_services<br>근거: 2행 · 근거.md:56 · tech_04_FBI_20261031.txt:8 · resp_16_DOJ_20261112.txt:15 · 「cryptocurrency exchange Binance」 | financial_services<br>근거: 2행 · 근거.md:106 · tech_04_FBI_20261031.txt:8 · tech_05_TRMLabs_20261029.txt:22 · 「cryptocurrency exchange Binance」 | 일치 | 두 코더 일치 · 그대로 |
| 42 | `victim_sector_sub_note` (자유 서술) | 주 표적(관측 범위 서술에서 방어국 미국을 겨냥한 적대 행위의 주된 피해 기관) = 암호화폐 거래소 바이낸스: 「cryptocurrency exchange Binance」(tech_04_FBI_20…<br>근거: 1행 · 근거.md:58 · tech_07_Elliptic_20261030.txt:34 · 「Binance, the world's largest cryptoasset exchange」 | 주 표적(방어국 = 미국 · 지시문 §3-4): 묶음이 서술하는 주된 피해 기관은 암호자산 거래소 바이낸스 하나 — 「cryptocurrency exchange Binance」(tech_04_FBI…<br>근거: 1행 · 근거.md:108 · tech_04_FBI_20261031.txt:8 · 「cryptocurrency exchange Binance」 | 서술 차이 | 코더 A의 문면 |
| 43 | `victim_assets` | [{"value": "Laptop Computer", "kind": "d3fend", "quote": "the security incident may involve a compromised DevO…<br>근거: 1행 · 근거.md:111 · tech_23_Binance_20261030.txt:9 · 「the security incident may involve a compromised DevOps engineer’s lapt…」 | [{"value": "Laptop Computer", "kind": "d3fend", "quote": "Our initial investigation suggests this security inc…<br>근거: 1행 · 근거.md:109 · tech_02_RichardTeng_20261030.txt:11 · 「Our initial investigation suggests this security incident may have sta…」 | 서술 차이 — 값 구조 같음 · quote · source만 다름 | 코더 A의 문면 |
| 44 | `identified_date` | 2026-11-12<br>근거: — (메타 키 · 행 불요) | 2026-11-12<br>근거: — (메타 키 · 행 불요) | 일치 | 두 코더 일치 · 템플릿 선기입 값 그대로(작업 규칙) |

- 「일치 여부」의 말: 일치 · 서술 차이(자유 서술 문면이 다름 · 또는 값 구조는 같고 인용 · 출처만 다름) · 값 불일치 · 한쪽 결측(한쪽만 비어 있음) · 코딩 대상 아님.

## 3. 집합 · 목록 키 상세

- `alias` — A 4: Jade Sleet, UNC4899, Slow Pisces, Pressure Chollima / B 4: Jade Sleet, UNC4899, Slow Pisces, Pressure Chollima · 공통 4 · A만 0 · B만 0
- `victim_sector` — A 1: finance_commerce / B 1: finance_commerce · 공통 1 · A만 0 · B만 0
- `victim_sector_sub` — A 1: financial_services / B 1: financial_services · 공통 1 · A만 0 · B만 0
- `c_id.source` — A: tech_04_FBI_20261031.txt; resp_16_DOJ_20261112.txt / B: tech_04_FBI_20261031.txt; resp_16_DOJ_20261112.txt
- `c_st.source` — A: resp_16_DOJ_20261112.txt; tech_04_FBI_20261031.txt / B: resp_16_DOJ_20261112.txt; tech_04_FBI_20261031.txt
- `victim_assets` — A: Laptop Computer(d3fend) · tech_23_Binance_20261030.txt:9 / B: Laptop Computer(d3fend) · tech_02_RichardTeng_20261030.txt:11

### 3-1. `legal_characterization` 값 구조별 항목 수(value — 서술 칸은 부록 B)

| 값 구조 | 코더 A | 코더 B |
|---|---:|---:|
| domestic_political_framing | 2 | 4 |

| value · source · 저자 검토 플래그 · quote 앞부분(항목 순) | 코더 A | 코더 B |
|---|---|---|
| 0 | domestic_political_framing · tech_04_FBI_20261031.txt:18 · True · 「identifying, mitigating, and disrupting North Korea's illici」 | domestic_political_framing · tech_04_FBI_20261031.txt:8 · True · 「The FBI refers to this specific North Korean malicious cyber」 |
| 1 | domestic_political_framing · resp_16_DOJ_20261112.txt:19 · True · 「we worked together to freeze this massive criminal fraud in 」 | domestic_political_framing · resp_17_외교부_20261105.txt:26 · True · 「북한의 불법 사이버 활동은 북한 핵·미사일 프로그램의 주요 자금원일 뿐 아니라 글로벌 디지털 경제에 대한 위」 |
| 2 | — | domestic_political_framing · resp_16_DOJ_20261112.txt:16 · True · 「North Korea’s government bankrolls its rogue regime and illi」 |
| 3 | — | domestic_political_framing · resp_16_DOJ_20261112.txt:19 · True · 「we worked together to freeze this massive criminal fraud in 」 |

### 3-2. `responses` 값 구조별 항목 수(type · subtype · actor_state · date · invoked_legal_basis · effect_at_response.value — 서술 칸은 부록 B)

| 값 구조 | 코더 A | 코더 B |
|---|---:|---:|
| criminal_investigation · ∅ · 미국 · 2026-10-31 · none_stated · post | 1 | 0 |
| public_attribution · ∅ · 미국 · 2026-10-31 · none_stated · post | 1 | 1 |
| criminal_investigation · ∅ · 미국 · 2026-11-12 · none_stated · post | 1 | 1 |
| public_attribution · ∅ · 미국 · 2026-11-12 · none_stated · post | 1 | 1 |

| 항목 순 · source | 코더 A | 코더 B |
|---|---|---|
| 0 | public_attribution · ∅ · 미국 · 2026-10-31 · none_stated · post · tech_04_FBI_20261031.txt | public_attribution · ∅ · 미국 · 2026-10-31 · none_stated · post · tech_04_FBI_20261031.txt |
| 1 | criminal_investigation · ∅ · 미국 · 2026-10-31 · none_stated · post · tech_04_FBI_20261031.txt | public_attribution · ∅ · 미국 · 2026-11-12 · none_stated · post · resp_16_DOJ_20261112.txt |
| 2 | public_attribution · ∅ · 미국 · 2026-11-12 · none_stated · post · resp_16_DOJ_20261112.txt | criminal_investigation · ∅ · 미국 · 2026-11-12 · none_stated · post · resp_16_DOJ_20261112.txt |
| 3 | criminal_investigation · ∅ · 미국 · 2026-11-12 · none_stated · post · resp_16_DOJ_20261112.txt | — |

## 4. 근거 파일 보조 대조 — 항목 밖 행(저자 확정 참고)

### 4-1. `c_st` 기준일과 첫 공식 귀속 성명일(지시문 §3 `c_st` · §4)

| 항목 | 코더 A | 코더 B | 두 코더 같음 |
|---|---|---|---|
| `c_st.reference_date` | 2026-11-12 | 2026-11-12 | 예 |
| `c_st.grade`(2026-11-12 기준 등급) | 5 | 5 | 예 |
| `c_st.reference_date` — 근거 md 행 | 2026-11-12 — 근거.md:49 · resp_16_DOJ_20261112.txt:6; 2026-11-12 — 근거.md:50 · resp_16_DOJ_20261112.txt:30 | 2026-11-12 — 근거.md:50 · resp_16_DOJ_20261112.txt:30; 2026-11-12 — 근거.md:51 · resp_16_DOJ_20261112.txt:6 | 같음(값 · 파일:줄 구성) |
| 첫 공식 귀속 성명일 — `c_st.basis`의 「첫 공식 귀속 성명일 YYYY-MM-DD」 | 2026-10-31 | 2026-10-31 | 예 |
| 첫 공식 귀속 성명일 — 근거 md `c_st.first_statement` 행 | 2026-10-31 — 근거.md:51 · tech_04_FBI_20261031.txt:8; 2026-10-31 — 근거.md:52 · tech_13_ReversingLabs_20261031.txt:110 | 2026-10-31 — 근거.md:52 · tech_04_FBI_20261031.txt:8; 2026-10-31 — 근거.md:53 · tech_13_ReversingLabs_20261031.txt:110; 2026-10-31 — 근거.md:54 · tech_07_Elliptic_20261030.txt:16 | 값은 같음 · 파일:줄 구성 다름(A만 없음 / B만 tech_07_Elliptic_20261030.txt:16) |
| 코더 안에서 basis 문구와 행의 날짜가 같은가 | 예 | 예 | 예 |
| 근거 성명이 여럿일 때 고른 날짜와 까닭(근거 md §3) | §3 「3-1. `c_st` 기준일 — 날짜가 다른 두 공식 성명」 | §3 3번 「`c_st` 기준일 규칙 적용」 | — |

### 4-2. `conflict_nexus` 요건별 판정(근거 md §1 · 지시문 §3-2)

| 요건 | 코더 A | 코더 B | 같음 |
|---|---|---|---|
| ⑴ 무장분쟁의 존재 (`conflict_nexus.req1`) | 구절 없음 — 근거.md:80 · — | 구절 없음 — 근거.md:81 · — | 예 |
| ⑵ 그 작전과 분쟁의 관련성 (`conflict_nexus.req2`) | 구절 없음 — 근거.md:81 · — | 구절 없음 — 근거.md:82 · — | 예 |
| ⑶ IHL 어휘의 원용이 관측 (`conflict_nexus.req3`) | 구절 없음 — 근거.md:82 · — | 구절 없음 — 근거.md:83 · — | 예 |
| 판정값 `conflict_nexus` | none | none | 예 |

### 4-3. 근거 md §1에서 근거 구절 칸에 「 」이 없는 행(표기 그대로 · 「묶음에 근거 없음」 행 제외)

- 코더 A · Claude Opus 0행 — 없음
- 코더 B · Claude Fable 0행 — 없음

### 4-4. `by_type` 값이 `pre`인데 근거 칸이 「묶음에 근거 없음」인 행(건수만 · 치환하지 않음)

- 코더 A · Claude Opus 0
- 코더 B · Claude Fable 0

### 4-5. 이 사례에서 더한 점검(지시문 §3-3 · §3-4 · §2)

**`effect_realized.by_type.1` · `by_type.2` 근거 행**(어느 칸이 맞는지는 적지 않는다)

| 칸 | 코더 A 행 | 코더 B 행 |
|---|---|---|
| `effect_realized.by_type.1` | post · tech_01_Binance_20261103.txt:83 · 「used the credentials stolen from Wallet DevOps Engineer A」<br>post · tech_01_Binance_20261103.txt:55 · 「However, Engineer A’s role and his related colleagues on our wallet infrastructure team w | post · tech_01_Binance_20261103.txt:83 · 「used the credentials stolen from Wallet DevOps Engineer A」<br>post · tech_01_Binance_20261103.txt:55 · 「However, Engineer A’s role and his related colleagues on our wallet infrastructure team w |
| `effect_realized.by_type.2` | post · tech_01_Binance_20261103.txt:41 · 「The attackers submitted 50 signing transactions to manipulate the account nonce and estab<br>post · tech_01_Binance_20261103.txt:27 · 「The attacker exploited unauthorized access to an internal wallet signing service to initi<br>post · tech_04_FBI_20261031.txt:8 · 「The Federal Bureau of Investigation (FBI) is releasing information advising the Democrati | post · tech_01_Binance_20261103.txt:29 · 「Between 20:05 UTC and 20:09 UTC, five Binance hot wallets sent 233.46 million XRP to an a<br>post · tech_01_Binance_20261103.txt:47 · 「The final unauthorized transfer of 2,961.9 ETH finalised on-chain at 23:56 UTC.」<br>post · tech_04_FBI_20261031.txt:8 · 「The Federal Bureau of Investigation (FBI) is releasing information advising the Democrati |
| `effect_realized.by_type.3` | pre · tech_02_RichardTeng_20261030.txt:27 · 「Temporarily suspended withdrawals while we complete a security revamp of the withdrawal s<br>pre · tech_02_RichardTeng_20261030.txt:24 · 「Deposits are unaffected and operating as normal」 | pre · tech_01_Binance_20261103.txt:39 · 「Binance immediately initiated multiple containment measures, including suspending withdra<br>pre · tech_02_RichardTeng_20261030.txt:24 · 「Deposits are unaffected and operating as normal」 |

**`victim_sector_sub` 첫 값(주 표적 · 방어국 = 미국) 근거 행**

| | 코더 A | 코더 B |
|---|---|---|
| 첫 값 | financial_services | financial_services |
| `victim_sector_sub` 행 | financial_services · tech_04_FBI_20261031.txt:8 · 「cryptocurrency exchange Binance」<br>financial_services · resp_16_DOJ_20261112.txt:15 · 「Binance, a virtual currency exchange」 | ["financial_services"] · tech_04_FBI_20261031.txt:8 · 「cryptocurrency exchange Binance」<br>["financial_services"] · tech_05_TRMLabs_20261029.txt:22 · 「Binance, the world's largest cryptocurrency exchange」 |
| `victim_state` | 미국(템플릿 값 그대로) | 미국(템플릿 값 그대로) |

**인용 금지 구간을 파일:줄로 든 곳** — 코더 A 0건 · 코더 B 0건(위 「기계 검사」 (다)).

## 부록 A. 값 안 인용 줄 보완(두 코더 똑같이 · 원 산출은 고치지 않는다)

> JSON 값 안의 「 」 인용 가운데 바로 뒤에 파일:줄이 없는 것. 묶음 25건에서 그 구절이 한 곳에만 있으면 그 줄을 적고(보완), 없거나 여러 곳이면 「줄 미상」.

| 코더 | 키 | 값 안 인용(앞부분) | 찾은 파일:줄 | 결과 |
|---|---|---|---|---|
| A(Opus) | `notes` | 「Contagious Interview, a North Korea-linked campaign」 | tech_14_SafeDep_20261103.txt:95 | 보완 |

## 부록 B. 두 코더의 값이 같지 않은 필드의 전체 값

### `c_id.basis`

- 코더 A(Opus):

```json
"식별 시점(2026-11-12) 등급 5 — 정부 문서가 이 작전을 단정 서술어로 TraderTraitor의 것으로 지목: FBI(2026-10-31) 「The FBI refers to this specific North Korean malicious cyber activity as \"TraderTraitor.\"」(tech_04_FBI_20261031.txt:8) · 미 법무부(2026-11-12) 「members of the North Korean military, referred to by the FBI as “TraderTraitor” stole more than $6 billion worth of virtual assets from the Binance cryptocurrency exchange」(resp_16_DOJ_20261112.txt:30). 그 전 시점(2026-10-29~30)은 보안업체 귀속 — TRM 「TRM attributes the attack to TraderTraitor, North Korea’s elite hacking unit, based on robust on and off-chain intelligence. We make this judgment with high confidence.」(tech_05_TRMLabs_20261029.txt:14) · Chainalysis 「Chainalysis attributes the hack to TraderTraitor, a North Korean cybercrime group.」(tech_08_Chainalysis_20261030.txt:20) · Elliptic은 FBI 발표 전 'likely'(tech_07_Elliptic_20261030.txt:24). 식별 시점 뒤의 상승: 묶음에 없음(자료 기준일 2026-11-12)."
```

- 코더 B(Fable):

```json
"식별 시점(2026-11-12) 기준 등급. 2026-10-31 FBI 경보가 수행 주체를 단정 서술 — 「The Federal Bureau of Investigation (FBI) is releasing information advising the Democratic People's Republic of Korea (North Korea) was responsible for the theft of more than $6 billion USD in virtual assets from cryptocurrency exchange Binance, on or about October 29, 2026.」(tech_04_FBI_20261031.txt:8) · 「The FBI refers to this specific North Korean malicious cyber activity as \"TraderTraitor.\"」(tech_04_FBI_20261031.txt:8). 2026-11-12 미 법무부 보도자료도 단정 서술 — 「members of the North Korean military, referred to by the FBI as “TraderTraitor” stole more than $6 billion worth of virtual assets from the Binance cryptocurrency exchange」(resp_16_DOJ_20261112.txt:30). 그 전의 보안업체 서술: 2026-10-29 TRM Labs 「TRM attributes the attack to TraderTraitor, North Korea’s elite hacking unit, based on robust on and off-chain intelligence. We make this judgment with high confidence.」(tech_05_TRMLabs_20261029.txt:14), 2026-10-30 Chainalysis 「Chainalysis attributes the hack to TraderTraitor, a North Korean cybercrime group.」(tech_08_Chainalysis_20261030.txt:20), Elliptic은 FBI 발표 전 「Elliptic had assessed TraderTraitor as the likely perpetrator before the announcement.」(tech_07_Elliptic_20261030.txt:24). 반대 방향 서술: 2026-10-30 Cointegrity 「TraderTraitor is the probable perpetrator, on circumstantial evidence.」(tech_10_Cointegrity_20261030.txt:40), 북한의 부인 「Kim Yo Jong, the sister of North Korean leader Kim Jong Un, rejected the FBI’s attribution in a statement carried by KCNA」(tech_17_Rekt_20261106.txt:425). 식별 시점 이후의 상승은 묶음에 없음(자료 기준일 2026-11-12)."
```

### `c_st.basis`

- 코더 A(Opus):

```json
"식별 시점(2026-11-12) 기준 등급 5(국가기관 소속 특정) — 미 법무부 보도자료(2026-11-12)가 수행자를 북한 군 소속으로 특정: 「members of the North Korean military, referred to by the FBI as “TraderTraitor” stole more than $6 billion worth of virtual assets from the Binance cryptocurrency exchange」(resp_16_DOJ_20261112.txt:30). 첫 공식 귀속 성명일 2026-10-31 — FBI 「The Federal Bureau of Investigation (FBI) is releasing information advising the Democratic People's Republic of Korea (North Korea) was responsible for the theft of more than $6 billion USD in virtual assets from cryptocurrency exchange Binance, on or about October 29, 2026.」(tech_04_FBI_20261031.txt:8; 날짜는 「On October 31, 2026, the FBI, the U.S. Secret Service and IRS Criminal Investigation attributed the theft to North Korea’s TraderTraitor.」 tech_13_ReversingLabs_20261031.txt:110). FBI 성명만 있던 2026-10-31~11-11 구간의 값은 4로 판단(국가 책임 단정 · 수행 기관 소속은 특정하지 않음). 보안업체 귀속(TRM·Chainalysis·Elliptic, 2026-10-29~30)은 공식 성명이 아니어서 등급 근거로 쓰지 않음. 북한 측 부인: tech_13_ReversingLabs_20261031.txt:110 · tech_17_Rekt_20261106.txt:425."
```

- 코더 B(Fable):

```json
"식별 시점(2026-11-12) 기준 등급. 2026-11-12 미 법무부 보도자료가 수행자를 국가기관(군) 소속으로 특정 — 「members of the North Korean military, referred to by the FBI as “TraderTraitor” stole more than $6 billion worth of virtual assets from the Binance cryptocurrency exchange」(resp_16_DOJ_20261112.txt:30), 같은 문서 「Today the Department of Justice announced coordinated actions against the Democratic People’s Republic of North Korea (DPRK) government’s schemes to fund its regime through the massive theft of cryptocurrency.」(resp_16_DOJ_20261112.txt:15). 첫 공식 귀속 성명일 2026-10-31 — FBI 경보 「The Federal Bureau of Investigation (FBI) is releasing information advising the Democratic People's Republic of Korea (North Korea) was responsible for the theft of more than $6 billion USD in virtual assets from cryptocurrency exchange Binance, on or about October 29, 2026.」(tech_04_FBI_20261031.txt:8); 그 성명의 날짜는 「On October 31, 2026, the FBI, the U.S. Secret Service and IRS Criminal Investigation attributed the theft to North Korea’s TraderTraitor.」(tech_13_ReversingLabs_20261031.txt:110)로 확인(FBI 문서 본문에는 게시일 표기가 없음). 첫 성명(2026-10-31)은 국가를 책임 주체로 단정하되 소속 기관은 특정하지 않음. reference_date에는 등급 5의 근거(기관 소속 특정)인 미 법무부 성명의 날짜를 적음."
```

### `access_depth.basis`

- 코더 A(Opus):

```json
"한 침투 안의 최댓값 = 내부 지갑 서명 서비스(특권 자산) 도달: 「The attacker exploited unauthorized access to an internal wallet signing service to initiate transactions outside the normal withdrawal process.」(tech_01_Binance_20261103.txt:27) · 「the attacker logged onto Software Engineer C’s computer, used the credentials stolen from Wallet DevOps Engineer A, deployed a container, and triggered a malicious script to launch the attack.」(tech_01_Binance_20261103.txt:83). 진입 벡터(엔지니어 업무용 컴퓨터)와 도달 자산(서명 서비스)을 구분했고, OT/ICS 자산은 묶음에 없음."
```

- 코더 B(Fable):

```json
"한 침투 안의 최댓값(관측 서술만). 2026-09 엔지니어 B의 업무용 컴퓨터 감염 「Engineer B was instructed to download an “assignment” containing a malicious code repository onto his work computer.」(tech_01_Binance_20261103.txt:63) → 2026-10-20 내부 AI 도구로 지갑 담당 엔지니어 A·C의 단말 장악 「The attacker leveraged the compromised computer of engineer B and used an internal AI tool to gain control over the Wallet DevOps Engineer A and another Wallet Software Engineer C.」(tech_01_Binance_20261103.txt:81) → 2026-10-29 탈취한 자격증명으로 컨테이너 배포 「On 29 October between 17:15 and 19:56, the attacker logged onto Software Engineer C’s computer, used the credentials stolen from Wallet DevOps Engineer A, deployed a container, and triggered a malicious script to launch the attack.」(tech_01_Binance_20261103.txt:83) → 내부 지갑 서명 서비스에 무단 접근해 정상 출금 절차 밖의 거래 개시 「The attacker exploited unauthorized access to an internal wallet signing service to initiate transactions outside the normal withdrawal process.」(tech_01_Binance_20261103.txt:27). 지갑 서명 서비스를 핵심 업무망의 특권 자산으로 보아 core. OT/ICS 구절은 묶음에 없음."
```

### `effect_realized.note`

- 코더 A(Opus):

```json
"유형 ②: 자산 탈취는 지시문 §3-3에 따라 유형 ②(조작·공개) 칸에서 판정 — 「The attackers submitted 50 signing transactions to manipulate the account nonce and establish malicious delegation authorizations.」(tech_01_Binance_20261103.txt:41) · 「The attacker exploited unauthorized access to an internal wallet signing service to initiate transactions outside the normal withdrawal process.」(tech_01_Binance_20261103.txt:27) · 「The Federal Bureau of Investigation (FBI) is releasing information advising the Democratic People's Republic of Korea (North Korea) was responsible for the theft of more than $6 billion USD in virtual assets from cryptocurrency exchange Binance, on or about October 29, 2026.」(tech_04_FBI_20261031.txt:8). 유형 ①: 자산 탈취와 별개로 엔지니어 컴퓨터에서 자격증명·토큰과 조직 정보가 탈취됨 — 「used the credentials stolen from Wallet DevOps Engineer A」(tech_01_Binance_20261103.txt:83) · 「However, Engineer A’s role and his related colleagues on our wallet infrastructure team was exposed to the hacker.」(tech_01_Binance_20261103.txt:55). 유형 ③: 공격자의 파괴·교란 효과 서술 없음 — 출금 중단은 피해자의 차단 조치이고 입금은 정상 — 「Temporarily suspended withdrawals while we complete a security revamp of the withdrawal service and its related addresses」(tech_02_RichardTeng_20261030.txt:27) · 「Deposits are unaffected and operating as normal」(tech_02_RichardTeng_20261030.txt:24). 경계: ①을 수단(자격증명 접근)으로 보아 pre로 둘지, ③을 출금 중단·'disruption'(tech_01_Binance_20261103.txt:9)으로 post로 둘지는 저자 확인 대상."
```

- 코더 B(Fable):

```json
"유형 ②(조작·공개): 지시문 §3-3에 따라 자산 탈취를 이 칸에서 판정 — 2026-10-29 20:05~23:56 UTC 핫월렛 자산이 공격자 주소로 이전 「Between 20:05 UTC and 20:09 UTC, five Binance hot wallets sent 233.46 million XRP to an attacker-controlled address.」(tech_01_Binance_20261103.txt:29) · 「The final unauthorized transfer of 2,961.9 ETH finalised on-chain at 23:56 UTC.」(tech_01_Binance_20261103.txt:47), 피해 규모 「Approximately USD 6.34 billion in digital assets were impacted by the incident.」(tech_01_Binance_20261103.txt:13) → post. 유형 ①(절취): 자산 탈취는 근거로 쓰지 않음. 탈취된 자격증명의 사용 「used the credentials stolen from Wallet DevOps Engineer A」(tech_01_Binance_20261103.txt:83)과 엔지니어 역할·동료 정보 노출 「However, Engineer A’s role and his related colleagues on our wallet infrastructure team was exposed to the hacker.」(tech_01_Binance_20261103.txt:55)을 정보 절취로 보아 post — 수단 단계의 절취라 판정이 갈릴 수 있음. 유형 ③(파괴·교란): 공격자가 피해 시스템을 파괴·교란했다는 구절은 없고 출금 중단은 바이낸스의 차단 조치로 서술됨 「Binance immediately initiated multiple containment measures, including suspending withdrawals to restrict further outflows」(tech_01_Binance_20261103.txt:39) → pre. 다만 바이낸스가 이용자에게 끼친 disruption을 언급하고 「This should not have happened, and we apologise for the concern, disruption and uncertainty it caused our users, partners and the wider industry.」(tech_01_Binance_20261103.txt:9) 출금 재개가 2026-11-01이어서 「November 1, 06:00 UTC: Binance announced it has begun reopening withdrawals, starting with $BTC Bitcoin network.」(tech_07_Elliptic_20261030.txt:14) ③ 판정을 경계 사례로 표시(boundary_flag=true). 종합값은 ②가 post이므로 post."
```

### `effect_realized.time_basis`

- 코더 A(Opus):

```json
"식별 시점 2026-11-12 기준(효과 발현: 자산 이동 2026-10-29 20:05~23:56 UTC — tech_01_Binance_20261103.txt:29 · tech_01_Binance_20261103.txt:47; 자격증명 탈취는 2026-10-20~29 — tech_01_Binance_20261103.txt:81 · tech_01_Binance_20261103.txt:83)"
```

- 코더 B(Fable):

```json
"식별 시점 2026-11-12 기준"
```

### `intrusion_state.basis`

- 코더 A(Opus):

```json
"식별 시점(2026-11-12)에 존속하는 무단 접근 서술 없음 — 2026-11-03 보고 기준 진입점 폐쇄·경로 시스템 재구축: 「The entry points identified as having been used in the attack have been closed. Systems touched in the attack path have been rebuilt or replaced.」(tech_01_Binance_20261103.txt:15); 마지막 무단 이체 2026-10-29 23:56 UTC 뒤 추가 이체 없음: 「No further unauthorised transfers were observed after.」(tech_01_Binance_20261103.txt:47); EIP-7702 위임 해제 2026-10-30 00:10 UTC: 「At 00:10 UTC on 30 October 2026, Binance executed a new authorization from the Binance14 hot wallet to the zero address, clearing the EIP-7702 delegation code.」(tech_01_Binance_20261103.txt:49). 탈취 자산의 세탁은 침해 밖의 활동이라 이 값의 근거로 쓰지 않음."
```

- 코더 B(Fable):

```json
"식별 시점(2026-11-12) 기준. 2026-10-29 23:56 UTC 마지막 무단 이체 뒤 추가 무단 이체 없음 「No further unauthorised transfers were observed after.」(tech_01_Binance_20261103.txt:47), 2026-10-30 00:10 UTC EIP-7702 위임 해제 「At 00:10 UTC on 30 October 2026, Binance executed a new authorization from the Binance14 hot wallet to the zero address, clearing the EIP-7702 delegation code.」(tech_01_Binance_20261103.txt:49), 2026-11-03 보고 기준 진입 지점 폐쇄·공격 경로 시스템 재구축 「The entry points identified as having been used in the attack have been closed. Systems touched in the attack path have been rebuilt or replaced.」(tech_01_Binance_20261103.txt:15), 관련 자격증명·토큰 폐기 「Decommissioned credentials and tokens related to affected engineers.」(tech_01_Binance_20261103.txt:95). 피해 기업의 자체 발표이고 조사는 진행 중 「The investigation remains ongoing and our findings will be subject to further independent review.」(tech_01_Binance_20261103.txt:17) — 독립 검토 결과는 묶음에 없음."
```

### `legal_characterization`

- 코더 A(Opus):

```json
[
 {
  "value": "domestic_political_framing",
  "quote": "identifying, mitigating, and disrupting North Korea's illicit cybercrime and virtual asset theft activities",
  "source": "tech_04_FBI_20261031.txt:18",
  "needs_author_review": true
 },
 {
  "value": "domestic_political_framing",
  "quote": "we worked together to freeze this massive criminal fraud in its tracks",
  "source": "resp_16_DOJ_20261112.txt:19",
  "needs_author_review": true
 }
]
```

- 코더 B(Fable):

```json
[
 {
  "value": "domestic_political_framing",
  "quote": "The FBI refers to this specific North Korean malicious cyber activity as \"TraderTraitor.\"",
  "source": "tech_04_FBI_20261031.txt:8",
  "needs_author_review": true
 },
 {
  "value": "domestic_political_framing",
  "quote": "북한의 불법 사이버 활동은 북한 핵·미사일 프로그램의 주요 자금원일 뿐 아니라 글로벌 디지털 경제에 대한 위협입니다.",
  "source": "resp_17_외교부_20261105.txt:26",
  "needs_author_review": true
 },
 {
  "value": "domestic_political_framing",
  "quote": "North Korea’s government bankrolls its rogue regime and illicit weapons program through cryptocurrency theft",
  "source": "resp_16_DOJ_20261112.txt:16",
  "needs_author_review": true
 },
 {
  "value": "domestic_political_framing",
  "quote": "we worked together to freeze this massive criminal fraud in its tracks",
  "source": "resp_16_DOJ_20261112.txt:19",
  "needs_author_review": true
 }
]
```

### `responses`

- 코더 A(Opus):

```json
[
 {
  "type": "public_attribution",
  "actor_state": "미국",
  "date": "2026-10-31",
  "invoked_legal_basis": "none_stated",
  "source": "tech_04_FBI_20261031.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점에 자산 탈취(2026-10-29 20:05~23:56 UTC)는 이미 발현 — 「The Federal Bureau of Investigation (FBI) is releasing information advising the Democratic People's Republic of Korea (North Korea) was responsible for the theft of more than $6 billion USD in virtual assets from cryptocurrency exchange Binance, on or about October 29, 2026.」(tech_04_FBI_20261031.txt:8)"
  }
 },
 {
  "type": "criminal_investigation",
  "actor_state": "미국",
  "date": "2026-10-31",
  "invoked_legal_basis": "none_stated",
  "source": "tech_04_FBI_20261031.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점에 자산 탈취(2026-10-29 20:05~23:56 UTC)는 이미 발현 — 「The Federal Bureau of Investigation (FBI) is releasing information advising the Democratic People's Republic of Korea (North Korea) was responsible for the theft of more than $6 billion USD in virtual assets from cryptocurrency exchange Binance, on or about October 29, 2026.」(tech_04_FBI_20261031.txt:8)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "미국",
  "date": "2026-11-12",
  "invoked_legal_basis": "none_stated",
  "source": "resp_16_DOJ_20261112.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점에 자산 탈취는 이미 발현 — 「members of the North Korean military, referred to by the FBI as “TraderTraitor” stole more than $6 billion worth of virtual assets from the Binance cryptocurrency exchange」(resp_16_DOJ_20261112.txt:30)"
  }
 },
 {
  "type": "criminal_investigation",
  "actor_state": "미국",
  "date": "2026-11-12",
  "invoked_legal_basis": "none_stated",
  "source": "resp_16_DOJ_20261112.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점에 자산 탈취는 이미 발현 — 「members of the North Korean military, referred to by the FBI as “TraderTraitor” stole more than $6 billion worth of virtual assets from the Binance cryptocurrency exchange」(resp_16_DOJ_20261112.txt:30)"
  }
 }
]
```

- 코더 B(Fable):

```json
[
 {
  "type": "public_attribution",
  "actor_state": "미국",
  "date": "2026-10-31",
  "invoked_legal_basis": "none_stated",
  "source": "tech_04_FBI_20261031.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2026-10-31)에 탈취 효과가 이미 발현 — 「The Federal Bureau of Investigation (FBI) is releasing information advising the Democratic People's Republic of Korea (North Korea) was responsible for the theft of more than $6 billion USD in virtual assets from cryptocurrency exchange Binance, on or about October 29, 2026.」(tech_04_FBI_20261031.txt:8). 성명일은 「On October 31, 2026, the FBI, the U.S. Secret Service and IRS Criminal Investigation attributed the theft to North Korea’s TraderTraitor.」(tech_13_ReversingLabs_20261031.txt:110)."
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "미국",
  "date": "2026-11-12",
  "invoked_legal_basis": "none_stated",
  "source": "resp_16_DOJ_20261112.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2026-11-12)에 탈취 효과가 이미 발현 — 「members of the North Korean military, referred to by the FBI as “TraderTraitor” stole more than $6 billion worth of virtual assets from the Binance cryptocurrency exchange」(resp_16_DOJ_20261112.txt:30)."
  }
 },
 {
  "type": "criminal_investigation",
  "actor_state": "미국",
  "date": "2026-11-12",
  "invoked_legal_basis": "none_stated",
  "source": "resp_16_DOJ_20261112.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2026-11-12)에 탈취 효과가 이미 발현 — 탈취 자산에 대한 법원 허가 압수·보전 「the court-authorized seizure and restraint of more than $1.2 billion worth of cryptocurrency recently stolen from Binance, a virtual currency exchange」(resp_16_DOJ_20261112.txt:15) · 「Collective U.S. government and private sector efforts so far have resulted in the freeze of more than $2.7 billion, with the Department having already obtained court-authorization to seize or restrain in excess of $1.2 billion of that amount.」(resp_16_DOJ_20261112.txt:30) · 「Efforts to trace, freeze, seize, and forfeit the stolen virtual assets are ongoing」(resp_16_DOJ_20261112.txt:31)."
  }
 }
]
```

### `aftermath`

- 코더 A(Opus):

```json
"식별 시점(2026-11-12) 이후의 후속: 묶음에 근거 없음(자료 기준일도 2026-11-12). 식별 시점에 진행 중으로 적힌 것 — 미 법무부(2026-11-12) 「Efforts to trace, freeze, seize, and forfeit the stolen virtual assets are ongoing, as TraderTraitor actors continue to launder such assets through various cryptocurrency bridges, mixers, and exchanges.」(resp_16_DOJ_20261112.txt:31) · 한국 외교부(2026-11-10) 독자 제재 등 추가 대응은 내부 검토 중·미확정(resp_18_외교부_20261110.txt:19)."
```

- 코더 B(Fable):

```json
""
```

### `boundary_flag`

- 코더 A(Opus):

```json
true
```

- 코더 B(Fable):

```json
false
```

### `boundary_reason`

- 코더 A(Opus):

```json
"효과 유형 경계 — 묶음은 이 사건을 'theft'(tech_04_FBI_20261031.txt:8)로 서술하나 저자 결정에 따라 자산 탈취를 유형 ②(조작·공개)로 판정했다(유형 ①과의 경계). ③(출금 중단·'disruption' tech_01_Binance_20261103.txt:9)도 경계. conflict_nexus는 none이라 그 요건과는 무관."
```

- 코더 B(Fable):

```json
""
```

### `notes`

- 코더 A(Opus):

```json
"⑴ 금전 동기(판정에 쓰지 않음): 「This group has repeatedly targeted the cryptocurrency industry, exchanges, DeFi protocols, and investors to raise funds for the regime.」(tech_08_Chainalysis_20261030.txt:30) · 「North Korea’s government bankrolls its rogue regime and illicit weapons program through cryptocurrency theft」(resp_16_DOJ_20261112.txt:16) · 「The US government has linked these thefts to the funding of North Korea’s weapons programs.」(tech_07_Elliptic_20261030.txt:40). ⑵ 벤더 쪽 법적 규정(격하): Cointegrity 「Until a government names North Korea, exposure to these funds is stolen-property risk. After an FBI statement or OFAC designation, the same exposure becomes sanctions risk」(tech_10_Cointegrity_20261030.txt:230). ⑶ 북한 부인: 김여정 KCNA 성명(tech_17_Rekt_20261106.txt:425) · tech_13_ReversingLabs_20261031.txt:110. ⑷ 행위자 경계: SafeDep은 면접 단계를 「Contagious Interview, a North Korea-linked campaign」로 봄(tech_14_SafeDep_20261103.txt:95) — RL은 「most vendors track Contagious Interview as a separate North Korean cluster, so the two are not the same claim.」(tech_13_ReversingLabs_20261031.txt:142). 법무부의 FaceStealer(Sapphire Sleet 등, resp_16_DOJ_20261112.txt:24)는 「Separately from the FaceStealer campaign」(resp_16_DOJ_20261112.txt:30)라 이 작전의 행위자·별칭에 넣지 않음. 'Lazarus umbrella'(tech_13_ReversingLabs_20261031.txt:142)는 상위 묶음 표현이라 alias에서 뺌. ⑸ Constella 로그(2026-03)는 「There is no evidence that this log was used in the attack.」(tech_19_Constella_20261111.txt:70) — 근거로 쓰지 않음. ⑹ 한국 외교부(2026-11-05·11-10)는 바이낸스 질의에 북한 불법 사이버 활동 일반으로 답하고 독자 제재 등을 검토 중이라고만 함(resp_17_외교부_20261105.txt:28 · resp_18_외교부_20261110.txt:19) — 공개 귀속·대응으로 넣지 않음."
```

- 코더 B(Fable):

```json
"[금전 동기] 묶음은 탈취 목적을 정권 자금 조달로 서술 — 「This group has repeatedly targeted the cryptocurrency industry, exchanges, DeFi protocols, and investors to raise funds for the regime.」(tech_08_Chainalysis_20261030.txt:30) · 미 법무부 「North Korea’s government bankrolls its rogue regime and illicit weapons program through cryptocurrency theft」(resp_16_DOJ_20261112.txt:16). 판정에 쓰지 않고 여기에만 둠. [행위자 표기] actor는 FBI 표기 그대로. ReversingLabs는 다른 이름과 상위 묶음을 함께 서술 — 「TraderTraitor, also tracked as Jade Sleet, UNC4899, Slow Pisces and Pressure Chollima, is a financially motivated North Korean cluster within the Lazarus umbrella.」(tech_13_ReversingLabs_20261031.txt:142) — Lazarus는 상위 묶음이라 alias에 넣지 않음. SafeDep의 Contagious Interview 평가는 별도 군집 서술이 있어 alias에 넣지 않음 — 「most vendors track Contagious Interview as a separate North Korean cluster」(tech_13_ReversingLabs_20261031.txt:142). 미 법무부 보도자료의 FaceStealer 부분은 이 사건과 별개로 서술되어 행위자·대응에서 뺌 — 「Separately from the FaceStealer campaign」(resp_16_DOJ_20261112.txt:30). [귀속에 대한 반응] 북한은 부인 — 「North Korea has denied involvement.」(tech_13_ReversingLabs_20261031.txt:110) · 「Kim Yo Jong, the sister of North Korean leader Kim Jong Un, rejected the FBI’s attribution in a statement carried by KCNA」(tech_17_Rekt_20261106.txt:425). [대한민국] 외교부 대변인은 2026-11-05·2026-11-10 정례브리핑에서 독자 제재 등 추가 방안을 검토 중이라고 답함 — 「사이버 독자 제재를 포함해서 추가적인 방안에 대해서 내부 검토 중이지만 아직 확정되지는 않았음」(resp_17_외교부_20261105.txt:28) · 「방금 말씀드린 사항은 계속 내부적으로 검토 중이고 확정된 바는 아직 없음」(resp_18_외교부_20261110.txt:19) — 이 사건을 북한에 귀속하는 명시 문장이 없고 실행된 조치가 아니어서 responses와 c_st 근거에 넣지 않음. [보안업체 규정] 업체들은 탈취·범죄로 서술(예: 「the largest crypto theft on record」(tech_06_Blockaid_20261029.txt:12)) — legal_characterization에 올리지 않음. [미국 관점] victim_state는 템플릿값 그대로. 묶음에는 미국 정부의 귀속·압수 조치 구절은 있으나 미국을 피해국으로 서술하는 구절은 없음. [묶음 간 수치 차이] 피해액은 약 63억~64.3억 달러, 동결액은 약 27억~30억 달러, 피해 체인 수는 10~11로 문서마다 다름."
```

### `target_specificity_basis`

- 코더 A(Opus):

```json
"바이낸스와 그 지갑 인프라 담당자를 특정해 겨냥: 「Software Engineer B had a profile on the platform that referenced his experience at Binance.」(tech_01_Binance_20261103.txt:59) · 「However, Engineer A’s role and his related colleagues on our wallet infrastructure team was exposed to the hacker.」(tech_01_Binance_20261103.txt:55) · 「the attacker used that mechanism to give an attacker-controlled smart contract partial execution rights over a Binance hot wallet.」(tech_01_Binance_20261103.txt:37)."
```

- 코더 B(Fable):

```json
"특정 기관(바이낸스)의 지갑 인프라 담당자를 겨냥한 침투 — 2026-06 지갑 DevOps 엔지니어 A의 역할·동료 노출 「However, Engineer A’s role and his related colleagues on our wallet infrastructure team was exposed to the hacker.」(tech_01_Binance_20261103.txt:55), 2026-09 바이낸스 경력을 프로필에 적은 엔지니어 B에게 접근 「Software Engineer B had a profile on the platform that referenced his experience at Binance.」(tech_01_Binance_20261103.txt:59), 2026-10-29 바이낸스 핫월렛에서 탈취 「Between 20:05 UTC and 20:09 UTC, five Binance hot wallets sent 233.46 million XRP to an attacker-controlled address.」(tech_01_Binance_20261103.txt:29)."
```

### `victim_sector_sub_note`

- 코더 A(Opus):

```json
"주 표적(관측 범위 서술에서 방어국 미국을 겨냥한 적대 행위의 주된 피해 기관) = 암호화폐 거래소 바이낸스: 「cryptocurrency exchange Binance」(tech_04_FBI_20261031.txt:8) · 「Binance, a virtual currency exchange」(resp_16_DOJ_20261112.txt:15) · 「Binance, the world's largest cryptoasset exchange」(tech_07_Elliptic_20261030.txt:34). 묶음에는 바이낸스와 미국의 관계(소재지·법인)를 적은 구절이 없다 — 미국 관점은 저자 결정의 메타 값. 다른 부문 피해 기관은 묶음에 없음(동결에 참여한 발행사·프로토콜은 대응 주체)."
```

- 코더 B(Fable):

```json
"주 표적(방어국 = 미국 · 지시문 §3-4): 묶음이 서술하는 주된 피해 기관은 암호자산 거래소 바이낸스 하나 — 「cryptocurrency exchange Binance」(tech_04_FBI_20261031.txt:8) · 「Binance, a virtual currency exchange」(resp_16_DOJ_20261112.txt:15) → financial_services(상위 finance_commerce). 묶음에 바이낸스의 소재국이나 미국 소재 피해 기관을 특정하는 구절은 없음. 2차 영향을 받은 곳(대출 프로토콜·스테이블코인 발행사 등)은 피해 기관으로 넣지 않음."
```

### `victim_assets`

- 코더 A(Opus):

```json
[
 {
  "value": "Laptop Computer",
  "kind": "d3fend",
  "quote": "the security incident may involve a compromised DevOps engineer’s laptop, which allowed an attacker to gain access to a service container",
  "source": "tech_23_Binance_20261030.txt:9"
 }
]
```

- 코더 B(Fable):

```json
[
 {
  "value": "Laptop Computer",
  "kind": "d3fend",
  "quote": "Our initial investigation suggests this security incident may have started with a compromised DevOps engineer's laptop.",
  "source": "tech_02_RichardTeng_20261030.txt:11"
 }
]
```
