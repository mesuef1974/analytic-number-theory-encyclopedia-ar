# المراجعة المستقلة لما قبل تأليف الفصل الثامن عشر

التاريخ: 2026-07-25

## نطاق المراجعة

تم تدقيق القرارات الرياضية المجمدة للفصل الثامن عشر، وبخاصة:

1. متباينة فرق فان دير كوربوت `ANT-LEM-18-02`.
2. اختبار المشتقة الأولى `ANT-THM-18-01`.
3. اختبارات الحالات الثابتة والخطية والتربيعية.
4. تدقيق عدم الدور مع الفصل السابع عشر.
5. الفصل بين النتائج المرشحة لـ`PROVED-HERE` والنتائج `CITED / EXPLAINED`.

## 1. متباينة فرق فان دير كوربوت

الصيغة المجمدة

\[
\left|\sum_{n=1}^{N}z_n\right|^2
\le
\frac{N+H-1}{H}
\left(
\sum_{n=1}^{N}|z_n|^2
+2\sum_{h=1}^{H-1}\left(1-\frac{h}{H}\right)
\left|\sum_{n=1}^{N-h}z_{n+h}\overline{z_n}\right|
\right)
\]

مطابقة للصيغة القياسية، بما في ذلك العامل الخارجي الحرج
\((N+H-1)/H\)، وحدود الارتباطات حتى `N-h`، والوزن `1-h/H`.

الحكم:

```text
ANT-LEM-18-02 = APPROVED AS PROVED-HERE TARGET
MATHEMATICAL-BLOCKERS = 0
```

## 2. اختبار المشتقة الأولى

الشرط الصحيح هو ضبط المسافة إلى أقرب عدد صحيح:

\[
\|f'(x)\|\ge \lambda>0,
\]

مع فرض الرتابة المناسب على `f'`، وليس مجرد الشرط `|f'(x)|\ge\lambda`.

المثال المضاد للشرط الخاطئ هو `f(x)=Mx` لعدد صحيح كبير `M`: عندئذ `|f'|=M` كبير، لكن `e(f(n))=1` لكل عدد صحيح `n`، فلا يحدث أي إلغاء.

الحكم:

```text
ANT-THM-18-01 = APPROVED AS PROVED-HERE TARGET
DISTANCE-TO-INTEGERS CONDITION = NECESSARY
MATHEMATICAL-BLOCKERS = 0
```

## 3. اختبارات الحالات

### الطور الثابت

إذا كان `f(x)=alpha`، فإن `f'=0` ولا يتحقق شرط `\|f'\|\ge\lambda>0`. وهذا متسق مع غياب الإلغاء.

### الطور الخطي

إذا كان `f(x)=alpha x`، فالمجموع هندسي، ويعطي التقدير القياسي

\[
\left|\sum e(\alpha n)\right|\ll \|\alpha\|^{-1},
\]

وهو متوافق مع اختبار المشتقة الأولى.

### الطور التربيعي

إذا كان `f(x)=alpha x^2+beta x`، فإن `f'` رتيبة و`f''=2alpha` ثابتة. لا يظهر تعارض بين الاختبارين الأول والثاني. أما المقارنة الكمية التفصيلية على مناطق التداخل فتُسجل بندًا أثناء التأليف، لا عائقًا لفتح البوابة.

## 4. عدم الدور

تدقيق عدم الدور مع الفصل السابع عشر صحيح:

- الفصل 18 يثبت أو يشرح أدوات عامة للمجاميع الأسية.
- الفصل 17 يبقي تقدير الأقواس الصغرى في وارينغ `CITED / COMPOSITE INPUT`.
- لا تحدث ترقية تلقائية لتصنيف نتائج الفصل 17.

```text
NONCIRCULARITY-AUDIT = PASS
CIRCULAR-DEPENDENCIES = 0
```

## 5. التصنيف العلمي

التقسيم الآتي متسق مع صعوبة الأدوات الفعلية:

```text
PROVED-HERE TARGETS:
- ANT-ID-18-01
- ANT-LEM-18-01
- ANT-LEM-18-02
- ANT-THM-18-01
- ANT-PROP-18-01 LIMITED VERSION

CITED / EXPLAINED:
- ANT-THM-18-02
- ANT-DEF-18-01 FRAMEWORK
- ANT-PROP-18-02
```

## الحكم النهائي

```text
REVIEW-TRACK           = INDEPENDENT PRE-AUTHORING
VERDICT                 = APPROVED
MATHEMATICAL-BLOCKERS   = 0
REFERENCE-BLOCKERS      = 0
NONCIRCULARITY-BLOCKERS = 0
PASS-FOR-AUTHORING      = YES
AUTHORING               = AUTHORIZED ON WORK BRANCH
MERGE                   = NOT AUTHORIZED
RELEASE-READY           = NO
```

هذا الحكم يفتح التأليف على فرع الفصل فقط. ولا يرفع أي نتيجة إلى `ACTIVE` أو الفصل إلى `REVIEWED` قبل اكتمال المتن والتدقيق والبناء والمراجعة اللاحقة.