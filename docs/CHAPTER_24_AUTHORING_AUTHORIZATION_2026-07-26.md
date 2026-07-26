# تفويض تأليف الفصل الرابع والعشرين

```text
CHAPTER                 = 24
VERSION                 = 0.28.0-dev
PRIMARY-REVIEW          = CHANGES-REQUIRED / 1 BLOCKER
BLOCKER-CORRECTION      = APPLIED
NARROW-RE-REVIEW       = PASS / 0 BLOCKERS
PASS-FOR-AUTHORING      = YES
AUTHORING               = AUTHORIZED ON CHAPTER BRANCH ONLY
RESULTS                 = 10 RESERVED / NON-CITABLE
MERGE                   = NOT AUTHORIZED
```

صدر حكم المراجعة المستقلة الضيقة في الالتزام:

```text
7fed8eb9dd3f69f4d43c2d5a720489b9f5a79830
```

وأثبت أن تصحيح صيغة هالاش الكمية مغلق بالكامل:

\[
\mathcal M(f;x,T)=\min_{|t|\le 2T}\mathbb D(f,n^{it};x)^2,
\]

وأن الحد المعتمد يتضمن كلا الجزأين

\[
(1+\mathcal M)e^{-\mathcal M}+T^{-1/2}.
\]

## نطاق التفويض

يسمح هذا القرار بكتابة متن الفصل 24، وإضافة ببليوغرافيته، وربطه بالمخطوط قبل خريطة الجبهات. لا يسمح بتفعيل النتائج أو اعتماد الفصل أو دمج PR #48.

## الحراس

- تبقى النتائج العشرة `RESERVED / NON-CITABLE`.
- لا توصف مبرهنة هالاش بأنها `PROVED-HERE`.
- لا يحذف الحد `T^{-1/2}` ولا يضيق مجال التصغير إلى `|t|<=T`.
- لا يستنتج الإلغاء إلا مع اختيار `T(x)\to\infty` وتباعد المقياس معًا.
- نتائج الفترات القصيرة والارتباطات مؤجلة ولا تدخل في إثبات النواة.
- تبقى خريطة الجبهات الفصل الأخير.
