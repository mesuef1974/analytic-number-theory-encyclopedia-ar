# الفصل الخامس عشر — إغلاق بوابة ما قبل التأليف

التاريخ: 2026-07-24

```text
CHAPTER                  = 15
VERSION                  = 0.19.0-dev
PRE-AUTHORING-GATE       = CLOSED
PASS-FOR-AUTHORING       = YES
OWNER-AUTHORIZATION      = NOT-YET-REQUIRED-FOR-DRAFT-AUTHORING
AUTHORING                = AUTHORIZED-AS-DRAFT
RESULTS                  = 9 / RESERVED
RELEASE-READY            = NO
```

## 1. الأدلة والمرجعيات

- أُنشئ سجل أدلة موسع.
- تحققت بيانات Greaves وRichert وOpera de Cribro وPolymath الأساسية.
- سُجل Erratum ورقة Polymath ولم تُنقل منه صيغة دون فحص.
- فُصل المصدر الأصلي عن المعالجة الكتابية وعن العرض الحديث.

## 2. التطبيع

اعتمد الفصل التطبيع:

\[
|\mathcal A_d|=Xg(d)+r_d,
\qquad
h(p)=\frac{g(p)}{1-g(p)},
\qquad
V(z)=\prod_{p<z}(1-g(p)),
\]

مع

\[
G(R,z)=\sum_{\substack{d<R\\d\mid P(z)}}\mu^2(d)h(d).
\]

كما فُصل حد الغربلة \(z\) عن مستوى البواقي \(D\) وعن البعد \(\kappa\).

## 3. المسار البرهاني

المسار المعتمد:

1. بيانات الغربال المجردة.
2. متراجحة المربع.
3. تحويل صورة سيلبرغ والتصغير المنتهي.
4. الحد العلوي \(X/G\) مع حد البواقي.
5. البعد الغربالي والحاصل المحلي.
6. اللمّة الأساسية بوصفها مدخلًا مقتبسًا مستقلًا.
7. عائق التكافؤ بصياغة تشخيصية محدودة.
8. تطبيق الأزواج المنخولة \(n(n+h)\).

## 4. التطبيق المركزي

لثابت زوجي \(h\ne0\):

\[
S_h(x,z)
=\#\{1\le n\le x:(n(n+h),P(z))=1\}
\ll_h\frac{x}{(\log z)^2}
\]

في المجال

\[
3\le z\le x^{1/4}.
\]

الحالة الفردية تنعدم عندما \(z>2\).

## 5. تدقيق عدم الدور

- البرهان المجرد مستقل عن Bombieri--Vinogradov.
- التطبيق المركزي مستقل عن Barban--Davenport--Halberstam.
- لا تستعمل الفجوات المحدودة أو حدسية الأوليات التوأم.
- لا يستعمل الاستنتاج النهائي نتيجة يراد إثباتها داخل الأداة نفسها.

الحكم:

```text
NO-CIRCULARITY = PASS
```

## 6. منشأ النتائج

- المتراجحة التربيعية والتصغير المنتهي والتطبيق: `PROVED-HERE`.
- تقدير \(G(z,z)\) العام واللمّة الأساسية: `CITED / COMPOSITE-INPUT`.
- عائق التكافؤ: `DIAGNOSTIC / CITED`.
- لا توجد نتائج مشروطة بـRH أو GRH.

## 7. حدود الادعاء

لا يدعي الفصل:

- إثبات حدسية الأوليات التوأم.
- إثبات فجوات محدودة.
- حدًا سفليًا موجبًا للأزواج الأولية.
- أن عائق التكافؤ استحالة مطلقة لكل طريقة غربالية.
- `RELEASE-READY`.

## 8. الحكم النهائي

```text
EVIDENCE-LEDGER          = PASS
NORMALIZATION-AUDIT      = PASS
PROOF-MAP                = PASS-FOR-DRAFT-AUTHORING
MINIMIZATION-AUDIT       = PASS
FUNDAMENTAL-LEMMA-ROUTE  = SELECTED
PARITY-BARRIER-AUDIT     = PASS
CENTRAL-APPLICATION      = SELECTED
FINAL-RANGE              = PASS
RESULTS                  = 9 / RESERVED
MATHEMATICAL-BLOCKERS    = 0
TEXTUAL-BLOCKERS         = 0
PRE-AUTHORING-GATE       = CLOSED
PASS-FOR-AUTHORING       = YES
AUTHORING                = AUTHORIZED-AS-DRAFT
RELEASE-READY            = NO
```
