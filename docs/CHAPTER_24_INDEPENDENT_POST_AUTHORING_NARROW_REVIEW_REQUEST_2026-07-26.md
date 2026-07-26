# طلب مراجعة مستقلة ضيقة لتصحيحات ما بعد تأليف الفصل الرابع والعشرين

## الرأس المطلوب مراجعته

```text
BRANCH                  = agent/chapter-24-pretentious-multiplicative-functions-v0.28.0
REVIEW-STAGE            = POST-AUTHORING NARROW RE-REVIEW
PRIMARY-POST-REVIEW     = CHANGES-REQUIRED / 0 BLOCKERS / 1 MAJOR / 1 MINOR
CORRECTIONS             = APPLIED
RESULTS                 = 10 AUTHORED-DRAFT / NON-CITABLE
OWNER-ADOPTION          = NOT REQUESTED
MERGE                   = NOT AUTHORIZED
```

## نطاق المراجعة الضيقة

راجع فقط التصحيحين الناتجين عن الالتزام المستقل:

- `3eacb0091b005e4e02e821765c69e0b933492da6`

وقارن متن الفصل بعد التصحيح مع الرأس السابق، ولا تعِد فتح العناصر التي اجتازت المراجعة ما لم يتسبب التصحيح في انزلاق جديد.

الملفات الحاكمة:

- `volumes/volume-15-modern-frontiers/chapters/chapter-24-pretentious-multiplicative-functions.tex`
- `docs/RESULTS_REGISTRY_CHAPTER_24.md`
- `docs/CHAPTER_24_INDEPENDENT_POST_AUTHORING_REVIEW_2026-07-26.md`

## الاختبارات المطلوبة

1. تحقق من صحة الرفع الاحتمالي: لكل `z = r e^{i theta}` في قرص الوحدة، المتغير الذي يأخذ `e^{i theta}` و`-e^{i theta}` باحتمالين `(1+r)/2` و`(1-r)/2` يحقق `|Z_z|=1` و`E Z_z=z`.
2. تحقق من أنه يمكن اختيار المتغيرات الخاصة بـ`f,g,h` مستقلة على فضاء احتمالي مشترك لكل أولي.
3. تحقق من الهوية
   \[
   \mathbb E|X_{f,p}-X_{g,p}|^2
   =2\bigl(1-\Re(f(p)\overline{g(p)})\bigr)
   \]
   باستعمال الاستقلال، لا بافتراض أن `f(p),g(p)` على دائرة الوحدة.
4. تحقق من أن مجموع هيلبرت المباشر الموزون بـ`1/(2p)` يمثل `\mathbb D(f,g;x)` بالضبط، وأن مينكوفسكي يعطي المتباينة المثلثية للحالة العامة `|f(p)|,|g(p)|,|h(p)| <= 1`.
5. تحقق من عدم إدخال افتراض استقلال غير متسق بين الأزواج الثلاثة، ومن أن فضاء واحدًا مشتركًا يكفي لتطبيق مينكوفسكي.
6. تحقق من أن مرجعي Elliott أصبحا مستشهدًا بهما في متن الفصل بالمفتاحين الصحيحين.
7. عد المعرفات وتأكد من بقائها عشرة بلا تكرار أو تغيير تصنيف.
8. أعد بناءً كاملًا بعد التصحيح، وسجل نجاح `xelatex -> biber -> xelatex -> xelatex`، وعدد الصفحات، وحل الاستشهادات، وترقيم الفصل 24 وخريطة الجبهات الأخيرة.

## صيغة الحكم المطلوبة

عند النجاح:

```text
VERDICT                 = PASS
BLOCKERS                = 0
MAJORS                  = 0
MINORS                  = 0
RESULTS-CITABLE         = NO
PASS-FOR-OWNER-ADOPTION = YES
MERGE-AUTHORIZED        = NO
```

وعند وجود خلل:

```text
VERDICT                 = CHANGES-REQUIRED
BLOCKERS                = <N>
MAJORS                  = <N>
MINORS                  = <N>
RESULTS-CITABLE         = NO
PASS-FOR-OWNER-ADOPTION = NO
MERGE-AUTHORIZED        = NO
```

يجب تسجيل كل ملاحظة مع درجتها والموضع والتصحيح المطلوب. لا يفعّل المراجع النتائج، ولا يعتمد الفصل نيابة عن المالك، ولا يدمج الفرع.
