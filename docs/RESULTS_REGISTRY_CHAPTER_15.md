# سجل نتائج الفصل الخامس عشر

آخر مراجعة: 2026-07-24

```text
CHAPTER                = 15
VERSION                = 0.19.0-dev
AUTHORING              = COMPLETE-AS-DRAFT
PASS-FOR-AUTHORING     = YES
CHAPTER-STATE          = REVIEWED
POST-AUTHORING-AUDIT   = PASS
REFERENCE-AUDIT        = PASS
INDEPENDENT-REVIEW     = APPROVED-WITH-NONBLOCKING-SYNC-CLOSED
REVIEWED-HEAD          = dee2013bce247522b298014f44dd3b07e795f922
RELEASE-READY          = NO
PR-28                  = DRAFT / OPEN / UNMERGED
```

| المعرّف | النتيجة | الحالة الحالية | المصدر أو البرهان |
|---|---|---|---|
| `ANT-DEF-15-01` | بيانات الغربال المجردة: \(P(z)\)، و\(S(\mathcal A,\mathcal P,z)\)، والتفكيك \(|\mathcal A_d|=Xg(d)+r_d\) | `DEFINITION / REVIEWED` | اصطلاح الفصل المثبت في تدقيق التطبيع |
| `ANT-LEM-15-01` | متراجحة المربع: \(S(\mathcal A,\mathcal P,z)\le\sum_{n\in\mathcal A}(\sum_{d\mid(n,P(z))}\lambda_d)^2\) عند \(\lambda_1=1\) | `PROVED-HERE / REVIEWED` | برهان مباشر من كون الوزن يساوي 1 على العناصر المنخولة |
| `ANT-THM-15-01` | الحد العلوي المنتهي لغربال سيلبرغ: \(S\le X/G(R,z)+\sum_{d<R^2}3^{\omega(d)}|r_d|\) | `PROVED-HERE / INDEPENDENTLY-CHECKED / REVIEWED` | التقطير الكامل، عكس موبيوس، كوشي--شفارتس، وصيغة معاملات سيلبرغ المثلى |
| `ANT-THM-15-02` | تقدير مقام سيلبرغ في بعد \(\kappa\): \(G(z,z)=e^{\gamma\kappa}V(z)^{-1}/\Gamma(\kappa+1)\,(1+O(1/\log z))\) | `CITED / TEXT-LOCATION-VERIFIED / NORMALIZATION-MATCHED / REVIEWED` | Heath-Brown ص. 21؛ Halberstam--Richert (5.3.1) |
| `ANT-THM-15-03` | اللمّة الأساسية العامة بصيغة أحادية \(S=XV(z)(1+O(\rho(s)))+\text{بواقي}\) | `CITED / CHAPTER-PAGE-RANGE-VERIFIED / NOT-USED-IN-PAIR-APPLICATION / REVIEWED` | Diamond--Halberstam--Galway، الفصل 4، ص 29--42 |
| `ANT-PROP-15-01` | الكثافة المحلية للأزواج \(n,n+h\): \(\rho_h(p)=2\) إذا \(p\nmid h\)، و\(1\) إذا \(p\mid h\)، مع انعدام الحالة الفردية بعد غربلة 2 | `PROVED-HERE / REVIEWED` | حساب فئات البواقي ومبرهنة الباقي الصيني |
| `ANT-PROP-15-02` | للحالة الزوجية \(h\ne0\)، يتحقق شرط الانتظام (15.6) بالبعد \(\kappa=2\)، و\(V_h(z)\asymp_h(\log z)^{-2}\) | `PROVED-HERE / INDEPENDENTLY-RECHECKED / REVIEWED` | برهان (15.12a) بمبرهنة ميرتنز الأولى، مع معالجة الأوليات القاسمة لـ\(h\) بحد \(O_h(1)\) |
| `ANT-THM-15-04` | لكل ثابت زوجي \(h\ne0\): \(S_h(x,z)\ll_h x/(\log z)^2\) بانتظام في \(3\le z\le x^{1/4}\) | `PROVED-HERE / INDEPENDENTLY-RECHECKED / REVIEWED` | تطبيق الحد المنتهي بعد التحقق الصريح من شرط (15.6)؛ الثابت فعّال من حيث المبدأ عند تثبيت \(h\) |
| `ANT-DIAG-15-01` | عائق التكافؤ: بيانات القواسم المحلية التقليدية لا تميز وحدها بما يكفي بين تكافؤ عدد العوامل الأولية | `DIAGNOSTIC / TEXT-LOCATION-VERIFIED / REVIEWED` | Friedlander--Iwaniec، ص 1042 و1044--1045 |

## حدود التسجيل

- لا تسجل حدسية الأوليات التوأم أو أي حد سفلي لعدد الأزواج الأولية.
- لا تسجل الفجوات المحدودة نتيجة للفصل.
- لا تسجل Brun--Titchmarsh ضمن المسار المركزي.
- لا تسجل صيغ \(F_\kappa(s),f_\kappa(s)\) بوصفها اللمّة الأساسية.
- حالة `REVIEWED` لا تعني `RELEASE-READY`، ولا تمنح إذنًا بدمج PR #28 أو تعديل `main`.

```text
RESULTS-AUTHORED        = 9
MATHEMATICAL-BLOCKERS   = 0
REFERENCE-BLOCKERS      = 0
GOVERNANCE-BLOCKERS     = 0
TEXTUAL-BLOCKERS        = 0
POST-AUTHORING-AUDIT    = PASS
REFERENCE-AUDIT         = PASS
INDEPENDENT-REVIEW      = APPROVED
CHAPTER-15              = REVIEWED
NEXT-ACTION             = OWNER-DECISION-ON-PR-28; NO-MERGE-WITHOUT-EXPLICIT-AUTHORIZATION
```
