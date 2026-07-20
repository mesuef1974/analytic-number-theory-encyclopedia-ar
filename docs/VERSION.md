# الإصدار الحالي

```text
0.17.0-dev
```

هذا الملف هو **المصدر الوحيد المعتمد لرقم الإصدار**. تُحدَّث النسخ المكررة في بقية الملفات بواسطة:

```powershell
.\scripts\sync-version.ps1
```

## معنى رقم الإصدار

- الرقم الأول: إصدار موسوعي رئيسي.
- الرقم الثاني: مرحلة علمية كبيرة أو فصل رئيسي.
- الرقم الثالث: تحديث تحريري أو تقني.
- اللاحقة `dev`: النسخة لا تزال قيد التطوير ولم تُعتمد للنشر.

## المرحلة الحالية

تستهدف `0.17.0-dev` الفصل الثالث عشر:

**مبرهنة بومبييري--فينوغرادوف والتوزيع المتوسطي للأعداد الأولية في المتتاليات الحسابية.**

```text
BASE-MAIN              = 607c6f8ad76f8085828f49ce6b566c846950ab2a
BRANCH                 = agent/chapter-13-bombieri-vinogradov-v0.17.0
MODE                   = EVIDENCE-FIRST / PRE-AUTHORING
CHAPTER-13             = PRE-AUTHORING
PRE-AUTHORING-GATE     = OPEN
AUTHORING              = BLOCKED
CENTRAL-TARGET         = BOMBIERI--VINOGRADOV / NOT YET ADOPTED
PROOF-ROUTE            = VAUGHAN-IDENTITY + LARGE-SIEVE / CANDIDATE
LEVEL-OF-DISTRIBUTION  = 1/2 WITH LOGARITHMIC LOSS / TARGET
DEPENDENCY-AUDIT       = OPEN
LOG-LOSS-AUDIT         = OPEN
EFFECTIVITY-AUDIT      = OPEN
RELEASE-READY          = NO
```

## الهدف المرشح

لكل \(A>0\) يوجد \(B=B(A)>0\) بحيث، عندما

\[
Q\le \frac{x^{1/2}}{(\log x)^B},
\]

تكون الكمية

\[
\sum_{q\le Q}\max_{(a,q)=1}\max_{2\le y\le x}
\left|\psi(y;q,a)-\frac{y}{\varphi(q)}\right|
\]

من رتبة \(O_A(x/(\log x)^A)\). هذه الصيغة هدف بحثي للفصل ولم تعتمد بعد نتيجة قابلة للاستشهاد.

## النزاهة البرهانية

- الغربال الكبير للشخصيات مرشح لأن يسجل `CITED` أو `COMPOSITE-INPUT` بعد التحقق المرجعي.
- هوية Vaughan مرشحة لبرهان داخلي.
- تقديرا Type I وType II ومبرهنة القيمة المتوسطة لم تغلق بعد.
- لا يدعي الفصل تجاوز حاجز \(1/2\).
- Elliott--Halberstam ونتائج الأوزان الخاصة بعد \(1/2\) خارج النطاق المركزي.
- لا يجوز بدء التأليف قبل إغلاق تدقيق الموصلات والحد الرئيسي والـ`max` والخسائر اللوغاريتمية والفعالية وعدم الدور.

## المرحلة السابقة

أُغلقت `0.16.0-dev` الخاصة بالفصل الثاني عشر علميًا وحوكميًا:

```text
CHAPTER-12          = REVIEWED / MERGED
PR-20               = MERGED
GOVERNANCE-PR-21    = MERGED
GOVERNANCE-MERGE    = 607c6f8ad76f8085828f49ce6b566c846950ab2a
LOCAL-SOURCE-BUILD  = PASS / 184 PAGES
RELEASE-READY       = NO
```
