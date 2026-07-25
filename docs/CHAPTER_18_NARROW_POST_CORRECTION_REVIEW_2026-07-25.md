# المراجعة الضيقة بعد التصحيح — الفصل الثامن عشر

التاريخ: 2026-07-25

## النطاق

راجعت المواضع الثلاثة التي حجبت اعتماد الرأس 018fa87، على الرأس:

    REVIEWED-HEAD = 7bc1364a12ba1b09cb93c971f9b80ed6d454d70b
    PR            = #35 / DRAFT / OPEN / UNMERGED

## التحقق

1. **لمّة كوسمين--لانداو:** تفترض الآن \(N\ge2\)، ويعالج برهان اختبار
   المشتقة الأولى حالة \(N\le1\) مباشرة من الحد التافه.
2. **المثال التربيعي:** يفرض الآن \(\alpha\ne0\)، ومن ثم
   \(\lambda=2|\alpha|>0\).
3. **ANT-DEF-18-01:** يعرف صراحة فئة الأطوار
   \(\mathcal F(N,P,\sigma,y,c)\)، ومجالات \(N,\sigma,y,P,c\)،
   وشروط المشتقات، والتقدير المنتظم
   \[
   \sum_{n\in I\cap\mathbb Z}e(f(n))
   \ll_{\kappa,\lambda,\sigma}
   \left(\frac{y}{N^\sigma}\right)^\kappa N^\lambda.
   \]
   يطابق هذا المعادلتين (1.1)--(1.2) في Trudgian--Yang.
4. يعيد الزوج التافه \((0,1)\) الحد \(O(N)\) حرفيًا.
5. تحويلا \(A\) و\(B\) في الفصل متسقان مع التطبيع المثبت.
6. مرجعا Trudgian--Yang وGraham--Kolesnik موجودان وقابلان للحل.

## التحقق الآلي والبصري

    QUALITY-CHECKS             = RUN-597 / SUCCESS
    PDF-BUILD                  = RUN-524 / SUCCESS
    PDF-PAGES                  = 249
    PDF-BYTES                  = 970373
    PDF-SHA256                 = 8E4270B0E6ED69D191D3755184F90A9565930C599ECCF9465DB2E1B1797617AA
    ARTIFACT-ZIP-SHA256        = C71EF648DAE7A7690B10E5E408CE25315A5207D5BC8B95FDA0098EDAB50998C0
    UNDEFINED-CITATIONS-FINAL  = 0
    UNDEFINED-REFERENCES-FINAL = 0
    VISUAL-AUDIT               = PASS

فُحصت بصريًا صفحات PDF 235--239 و249. لم يظهر قص أو تراكب أو كسر
للمعادلات أو شارات المراجع.

## الحكم

    NARROW-REVIEW    = PASS
    MAJOR-BLOCKERS   = 0
    MINOR-BLOCKERS   = 0
    CHAPTER-18       = REVIEWED-CANDIDATE / OWNER-ADOPTION-PENDING
    CITABILITY       = NON-CITABLE
    PR-35            = DRAFT / OPEN / UNMERGED
    MERGE            = NOT AUTHORIZED
    RELEASE-READY    = NO

هذا الحكم يغلق بنود CHANGES-REQUIRED، لكنه لا يساوي اعتماد المالك ولا
يمنح إذن الدمج.
