# طلب المراجعة المستقلة للفصل العشرين — 2026-07-25

## هدف المراجعة المثبت

\`\`\`text
REPOSITORY        = mesuef1974/analytic-number-theory-encyclopedia-ar
PULL-REQUEST      = #39
BRANCH            = agent/chapter-20-modular-maass-trace-formulas-v0.24.0
SCIENTIFIC-HEAD   = 46ac3dfee46bb0abe2a43459c55041d5773ed78e
QUALITY           = #682 / SUCCESS
PDF               = #596 / SUCCESS
AUTHORING         = BLOCKED
MERGE             = NOT AUTHORIZED
\`\`\`

الرأس العلمي المثبت هو آخر رأس يضم مطابقة Petersson وKuznetsov وSelberg وتحديث ملفات الحوكمة. ملف الطلب نفسه وما يتبعه من بيانات مراجعة إدارية ليس جزءًا من الهدف العلمي إلا إذا عدّل مصدرًا أو صيغة.

## شرط الاستقلال

على المراجع أن يصرح بأنه لم يؤلف حزمة المطابقة محل الحكم، وأن يذكر إن كان اعتماده على قراءة المصادر الأصلية/الكاملة مباشرًا أو على تحقق ثانوي. لا يجوز لمؤلف الحزمة منحها حكم الاستقلال.

## الملفات الإلزامية

1. \`docs/CHAPTER_20_EVIDENCE_LEDGER_2026-07-25.md\`
2. \`docs/CHAPTER_20_NORMALIZATION_TABLE_2026-07-25.md\`
3. \`docs/CHAPTER_20_PROOF_MAP_2026-07-25.md\`
4. \`docs/CHAPTER_20_PRE_AUTHORING_AUDIT_2026-07-25.md\`
5. \`docs/CHAPTER_20_KUZNETSOV_CROSSCHECK_2026-07-25.md\`
6. \`docs/CHAPTER_20_SELBERG_CROSSCHECK_2026-07-25.md\`
7. \`docs/CHAPTER_20_CONSENSUS_DISCOVERY_2026-07-25.md\`

## مصفوفة الحكم

| الاختبار | المطلوب | الحكم |
|---|---|---|
| Petersson | مطابقة المستوى \(1\): القطري، \(\Gamma(k-1)\)، \(i^{-k}\)، نواة \(J_{k-1}\)، وتطبيع حاصل الضرب | PENDING |
| Kuznetsov | توسع مااس، الطيف المنفصل والمستمر، القطري، Kloosterman، وتحويل \(J\) للإشارة المتساوية | PENDING |
| سياق \(K\)-Bessel | التأكد من أنه لم يُخلط بالنواة الأساسية وأنه محصور في الإشارة المتعاكسة | PENDING |
| Selberg | زوج التحويل وعامل \(2\pi\)، حد المساحة، كثافة Plancherel، والحد الجيوديسي | PENDING |
| حد النطاق | Selberg المدمج لا يُعرض بوصفه صيغة المجموعة المعيارية غير المدمجة | PENDING |
| المصادر | كل ثابت دقيق يعود إلى نص كامل/موضع مثبت؛ Consensus قناة اكتشاف لا بديل استشهاد | PENDING |
| عدم الدور | لا اعتماد عكسي على الفصل 21 ولا استعمال لنتيجة لاحقة لإثبات مدخل سابق | PENDING |
| الحوكمة | لا متن، ولا ترقية نتائج، ولا دمج قبل الحكم | PENDING |

## أسئلة مانعة

1. هل جميع التحويلات والثوابت متسقة داخل اصطلاح واحد؟
2. هل توجد أي مساواة صحيحة فقط بعد إعادة تطبيع غير مصرح بها؟
3. هل حُذف طيف Eisenstein من Kuznetsov أو نُقل نموذج Selberg المدمج إلى حالة غير مدمجة؟
4. هل يثبت سجل الأدلة الفرق بين التحقق الببليوغرافي ومطابقة الصيغة؟
5. هل تكفي الحزمة لبدء تأليف عرض مضبوط ضمن النطاق المعلن، لا أوسع منه؟

## صيغة الحكم المطلوبة

\`\`\`text
REVIEWER-INDEPENDENCE = CONFIRMED | NOT CONFIRMED
SCIENTIFIC-VERDICT    = PASS | CHANGES-REQUIRED
BLOCKERS              = <integer>
MAJOR                 = <integer>
MINOR                 = <integer>
PASS-FOR-AUTHORING    = YES | NO
REVIEWED-HEAD         = 46ac3dfee46bb0abe2a43459c55041d5773ed78e
\`\`\`

كل ملاحظة يجب أن تسمي الملف والموضع، وتبين أثرها: ثابت خاطئ، نطاق زائد، مصدر غير كافٍ، اعتماد دائري، أو تحسين غير حاجز.

## قاعدة الانتقال

لا يُغيّر \`AUTHORING = BLOCKED\` إلا إذا كان الاستقلال مؤكدًا، والحكم \`PASS\`، وعدد العوائق صفرًا، ثم سُجل \`PASS-FOR-AUTHORING = YES\` صراحةً. لا يمنح هذا الحكم إذن دمج.
