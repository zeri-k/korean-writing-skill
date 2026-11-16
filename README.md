# Korean Writing Skill

문서의 의미와 기술적 정확성을 보존하며 명확한 한국어를 작성·교정하는 AI 에이전트 스킬입니다. 문서 작성, 번역, 요약과 상세 문장 교정에 사용합니다.

- 배포 버전: **1.0.1**
- 스킬 이름: `korean-writing`
- 라이선스: [MIT](LICENSE)

## 주요 기능

- 사실, 조건, 수치, 시제와 기술적 의미를 보존합니다.
- 대상과 수행 동작, 근거와 결과 사이의 관계를 명확히 설명합니다.
- 문서 목적과 예상 독자에 맞춰 표현, 설명 깊이와 약어 풀이를 조정합니다.
- 기술 용어는 해당 분야와 독자에게 통용되는 한국어, 영어 또는 한글 음역을 선택합니다.
- 과장과 불필요한 강조를 줄이고, 확인한 결과와 가능성·추정을 구분합니다.
- 사용자 수정본을 후속 교정의 기준으로 삼습니다.
- 작업에 필요한 참조 문서만 읽도록 구성되어 있습니다.

## 적용 범위

보고서, 기술 문서, PPT 문구와 발표 노트, 매뉴얼, 메일 등의 한국어 작성과 교정에 사용할 수 있습니다. 일반 질의응답이나 단순 맞춤법 확인에는 자동 적용하지 않도록 설명되어 있으며, 스킬을 명시하면 짧은 문장에도 적용할 수 있습니다. 자동 선택 여부는 사용하는 에이전트의 스킬 기능에 따라 달라집니다.

이 프로젝트의 격식체, 기호와 용어 선택은 **스킬을 적용할 때 사용하는 편집 기본값**입니다. 한국어 전체의 규범으로 제시하는 기준은 아니며, 사용자 요청과 문서의 명시적 기준이 우선합니다. 기술·보안 분야의 예시가 포함되어 있지만, 예시에 등장하는 표현을 모든 문서의 금칙어나 필수 형식으로 취급하지 않습니다.

`실제`가 강조만 더하면 생략할 수 있지만, 모의훈련과 실제 사고를 구분할 때는 유지합니다. 약어 풀이도 예상 독자에게 필요한 경우에 추가합니다.

## 설치

### Codex의 프로젝트별 설치

사용할 프로젝트의 루트에서 다음 명령으로 `v1.0.1`을 설치할 수 있습니다. Git이 필요하며, 설치 대상 폴더가 이미 있는 경우에는 기존 내용을 먼저 확인합니다.

```sh
git clone --branch v1.0.1 --depth 1 https://github.com/zeri-k/korean-writing-skill.git .agents/skills/korean-writing
```

설치 결과는 다음과 같습니다.

```text
프로젝트/
└── .agents/
    └── skills/
        └── korean-writing/
            ├── SKILL.md
            └── references/
```

Codex는 프로젝트의 `.agents/skills`에서 로컬 스킬을 탐색합니다. 새 스킬이 표시되지 않으면 Codex를 다시 시작할 수 있습니다. 사용자 전체에 설치하는 경로와 다른 설치 방법은 [공식 스킬 문서](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)에서 확인할 수 있습니다.

다른 AI 에이전트에서 사용할 때는 해당 도구의 `SKILL.md` 지원 여부와 설치 경로를 확인합니다. 스킬 본문과 `references/` 폴더의 상대경로를 유지해야 합니다.

## 사용 예시

### 문장 교정

```text
$korean-writing
아래 문장을 검토해줘. 사실과 기술적 의미는 유지하고,
독자가 추정해야 하는 연결과 불필요한 강조를 정리해줘.
```

### 기술 문서 작성

```text
$korean-writing
아래 조사 결과를 개발자 대상 보고서로 작성해줘.
확인된 사실과 추정, 조치 제안과 적용 완료를 구분해줘.
```

### 사용자 수정본을 기준으로 재검토

```text
$korean-writing
내가 수정한 본문을 기준으로 문장 연결을 검토해줘.
수행 시점과 대상 범위를 유지하고, 추가 근거가 필요한 부분은 알려줘.
```

## 파일 구성

| 파일 | 역할 |
|---|---|
| [SKILL.md](SKILL.md) | 적용 범위, 참조 문서 선택과 공통 판단 기준 |
| [house-style.md](references/house-style.md) | 문체, 표기와 어휘의 편집 기본값 |
| [document-style.md](references/document-style.md) | 문서 목적에 따른 내용 선택과 형식 |
| [prose.md](references/prose.md) | 문장 관계, 어순과 군더더기 검토 |
| [terminology.md](references/terminology.md) | 기술 용어, 약어와 대상의 명칭 |
| [evidence.md](references/evidence.md) | 근거, 시점·범위와 주장 강도의 보존 |
| [numbers.md](references/numbers.md) | 집계 수치, 비율과 비교 기준 |
| [procedures.md](references/procedures.md) | 절차의 입력·결과와 코드 설명의 대응 |
| [presentation.md](references/presentation.md) | PPT 발표 노트와 발표 대본 |

## 버전과 변경 제안

배포 버전은 [VERSION](VERSION)과 `SKILL.md`의 `metadata.version`에 기록하며, Git 태그는 `v1.0.1` 형식을 사용합니다. 변경 이력은 [CHANGELOG.md](CHANGELOG.md)에 기록합니다. `KOREAN-WRITING-COMMON` 식별자는 같은 공통 스타일 본문을 중복해서 읽지 않기 위한 기준이므로, 공통 스타일을 수정할 때는 `SKILL.md`와 `house-style.md`의 식별자를 함께 확인합니다.

변경 제안에는 원문, 의도한 의미와 예상 독자, 문제가 된 표현을 포함하면 판단에 도움이 됩니다. 한 문서의 편집 선호를 모든 문서에 적용하는 규칙으로 확대하지 않는 것을 원칙으로 합니다.

## 라이선스

[MIT License](LICENSE)를 적용합니다.
