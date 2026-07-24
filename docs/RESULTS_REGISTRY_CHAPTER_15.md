# سجل نتائج الفصل الخامس عشر

آخر مراجعة: 2026-07-24

```text
CHAPTER                = 15
VERSION                = 0.19.0-dev
AUTHORING              = COMPLETE-AS-DRAFT
PASS-FOR-AUTHORING     = YES
CHAPTER-STATE          = AUTHORED-DRAFT
POST-AUTHORING-AUDIT   = PENDING
RELEASE-READY          = NO
```

| المعرّف | النتيجة | الحالة الحالية | المصدر أو البرهان |
|---|---|---|---|
| `ANT-DEF-15-01` | بيانات الغربال المجردة: \(P(z)\)، و\(S(\mathcal A,\mathcal P,z)\)، والتفكيك \(|\mathcal A_d|=Xg(d)+r_d\) | `DEFINITION / AUTHORED-DRAFT` | اصطلاح الفصل المثبت في تدقيق التطبيع |
| `ANT-LEM-15-01` | متراجحة المربع: \(S(\mathcal A,\mathcal P,z)\le\sum_{n\in\mathcal A}(\sum_{d\mid(n,P(z))}\lambda_d)^2\) عند \(\lambda_1=1\) | `PROVED-HERE / AUTHORED-DRAFT` | برهان مباشر من كون الوزن يساوي 1 على العناصر المنخولة |
| `ANT-THM-15-01` | الحد العلوي المنتهي لغربال سيلبرغ: \(S\le X/G(R,z)+\sum_{d<R^2}3^{\omega(d)}|r_d|\) | `PROVED-HERE / AUTHORED-DRAFT` | تحويل الصورة التربيعية، كوشي--شفارتس، واختيار سيلبرغ الأمثل |
| `ANT-THM-15-02` | تقدير مقام سيلبرغ في بعد \(\kappa\): \(G(z,z)=e^{\gamma\kappa}V(z)^{-1}/\Gamma(\kappa+1)\,(1+O(1/\log z))\) | `CITED / COMPOSITE-INPUT / AUTHORED-DRAFT` | Halberstam--Richert ومعالجات الغربال القياسية؛ الموضع الدقيق يثبت في التدقيق المرجعي |
| `ANT-THM-15-03` | اللمّة الأساسية العامة للغربال في صيغة واحدة مختارة | `CITED / COMPOSITE-INPUT / AUTHORED-DRAFT` | Opera de Cribro أو Diamond--Halberstam--Galway بعد تثبيت الصياغة النهائية |
| `ANT-PROP-15-01` | الكثافة المحلية للأزواج \(n,n+h\): \(\rho_h(p)=2\) إذا \(p\nmid h\)، و\(1\) إذا \(p\mid h\)، مع انعدام الحالة الفردية بعد غربلة 2 | `PROVED-HERE / AUTHORED-DRAFT` | حساب فئات البواقي ومبرهنة الباقي الصيني |
| `ANT-PROP-15-02` | للحالة الزوجية \(h\ne0\)، يكون البعد الغربالي \(\kappa=2\) و\(V_h(z)\asymp_h(\log z)^{-2}\) | `PROVED-HERE / AUTHORED-DRAFT` | تحليل العوامل المحلية مع مبرهنة ميرتنز |
| `ANT-THM-15-04` | لكل ثابت زوجي \(h\ne0\): \(S_h(x,z)\ll_h x/(\log z)^2\) بانتظام في \(3\le z\le x^{1/4}\) | `PROVED-HERE / AUTHORED-DRAFT` | `ANT-THM-15-01` و`ANT-THM-15-02` وحساب البواقي المحلي |
| `ANT-DIAG-15-01` | عائق التكافؤ: بيانات القواسم المحلية التقليدية لا تميز وحدها بما يكفي بين تكافؤ عدد العوامل الأولية | `DIAGNOSTIC / CITED / AUTHORED-DRAFT` | Opera de Cribro، ومعالجة Selberg/Polymath الحديثة مع حدود الادعاء |

## حدود التسجيل

- لا تسجل حدسية الأوليات التوأم أو أي حد سفلي لعدد الأزواج الأولية.
- لا تسجل الفجوات المحدودة نتيجة للفصل.
- لا تسجل Brun--Titchmarsh ضمن المسار المركزي.
- لا تسجل صيغ \(F_\kappa(s),f_\kappa(s)\) قبل اختيار تطبيعها النهائي.
- لا تصبح النتائج `VERIFIED` قبل تدقيق ما بعد التأليف والتحقق المرجعي والبناء.

```text
RESULTS-AUTHORED       = 9
MATHEMATICAL-BLOCKERS  = 0 / PRE-AUDIT
TEXTUAL-BLOCKERS       = 0 / PRE-AUDIT
PASS-FOR-AUTHORING     = YES
NEXT-ACTION            = POST-AUTHORING-AUDIT
```
