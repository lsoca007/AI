# Project 1: Constrained Satisfaction & Backtracking
___

## Introduction
In classic sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and
each of the nine 3 × 3 subgrids that compose the grid (also called "boxes", "blocks", or "regions")
contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a
well-posed puzzle has a single solution.

Sudoku has 81 variables, i.e., 81 tiles. The variables are named by row and column and are valued from 1 to 9 subject to the constraints that two cells in the same row, column, or box may be the same.
Frame your problem in terms of variables, domains, and constraints. We will represent a Sudoku using a Python dictionary or hash map, where each key is a variable name based on location, and value of the tile placed there. For instance, for the Sudoku above, we have the following:
• sudoku_dict[“B3”] = 7
• sudoku_dict[“F1”] = 7
• sudoku_dict[“D1”] = 0 (we assign 0 to empty cells)

## Project Description

Backtracking Algorithm
Implement backtracking search using the minimum remaining value heuristic. Pick your own order of values to try for each variable and apply forward checking to reduce variables domains.

## Use

The program needs to execute as follows:\
`python3 sudoku.py <input_string>`

The file named sudoku_boards.txt that contains samples of unsolved Sudoku boards, and sudoku_boards_solved.txt with their corresponding solutions. Each board is represented as a single line of text, starting from the top-left corner of the board, and listed left-to-right, top-to- bottom.
For instance, the string
003020600900305001001806400008102900700000008006708200002609500800203009005010300
is equivalent to the following Sudoku board:

003020600\
900305001\
001806400\
008102900\
700000008\
006708200\
002609500\
800203009\
005010300

The program will generate output.txt, containing a single line of text representing the finished Sudoku board. E.g.:\
483921657967345821251876493548132976729564138136798245372689514814253769695417382
___

## Testing Results

All sudoku boards from sudoku_boards.txt were solved successfully 

Finishing all boards in file.
Time: --- 27.591152906417847 seconds ---

Output:\
483921657967345821251876493548132976729564138136798245372689514814253769695417382
435269781682571493197834562826195347374682915951743628519326874248957136763418259
956138742237954816481672953594867321128593674763421598879246135312785469645319287
794582136268931745315476982689715324432869571157243869821657493943128657576394218
249186573735942186168375429512697348976834251483251967694723815327518694851469732
653287941794631258128945376819724563236859417547163829965372184372418695481596732
152479683368215974974638512416387259783952461529146837237864195891523746645791328
894317265731526894562984173358642719247139586619758432173465928925873641486291357
168295374529734618437186529312578496875649132694312785786951243951423867243867951
597468132318927564642153897456832971821796345973514628735641289164289753289375416
379521684284736519651498372732845961548619723196273845917364258425987136863152497
526394871817652349394817526148736952632985714759421683975143268281569437463278195
742698513816523947539714682381952764965847231427136859653479128174285396298361475
184726539376859142925413786652137498713984625849265317591372864468591273237648951
715986423689243715324175968963418572841752639257639184132564897596827341478391256
156938427427156938398472561534689712869217354712543896243891675675324189981765243
582946731934187625671235849168492357345768912729513486456871293293654178817329564
623815947479236185851794326934678251718952634265143798596387412142569873387421569
762149853385672914194583762527316498946827531831954276453768129219435687678291345
128397546397654812654218937786531294942786351513942678469875123875123469231469785
569143287287965431413872695635729148872514963941386752326457819154298376798631524
746912358921358746538467219689745123317286594452139687873591462265874931194623875
675913482482657931391248675817362549263594718954781326749125863528436197136879254
549283671678941352321567948185492736937816524264375189413729865856134297792658413
539472816276183954148569723492736581851924637367815249615398472724651398983247165
286145793579632184134789256425896371618327945793514628862951437347268519951473862
567128349934657182281493576346875291752916438819342765195764823423589617678231954
382746519467519832915283647254897361731625984896431725543962178629178453178354296
641352897325987641978461352259836714783149265164275983836714529497528136512693478
489356172536721849712984536197435628348162795625879314273548961954613287861297453
167523849984176523325489671798315264642798135531642798476831952213957486859264317
293518746851476293476923518512384967687159432349762185164235879728691354935847621
617329584398457621425618739286174953953286147174593862762831495549762318831945276
859632147236174859741895632125948376974326581368517924493781265687259413512463798
496175382785342196312986457547891623823654719961237548178423965659718234234569871
318624579624759183759183264286947351475231896931865742867412935592376418143598627
915823746728465319634719582159347268286591473347682195593178624472936851861254937
581497632796235148432168957875914326624783519319526874943852761167349285258671493
513628794682497351794531628836159247457362189129874536975286413348715962261943875
637518294518492736429367518954783162783621459162945873876134925295876341341259687
354218697218976354769453812496321578527869143831745926945632781173584269682197435
369415782175892364428367195234179856791586243586234917847621539953748621612953478
927145683146837952358962174581694327694723815273581469769358241812479536435216798
392815476165437892487269153214378569873956214956142738538794621749621385621583947
198576432756423981423891657671935248842617593935284716287359164514768329369142875
485126937162397845937584126216973458793845612548612379351768294674239581829451763
425681937793542186168973425972315648531864279846729351289137564317456892654298713
187624593652389174439157682814795326526831947793462851975216438268943715341578269
869172354721453689435896127172685493596347812348921576283714965617539248954268731
952346178463781952178529364846197235521463897739258641297615483615834729384972516
487536192612894357593172468348259671761348925925761843839427516256913784174685239
291643758643875291857291436536127849179458623428936517714569382382714965965382174
539481276148276359267593814623714985895632147471958632914325768352867491786149523
279156834148739526536284917685913742394872651721465398917328465853641279462597183
715496823483217956962835147634159278891372465527648391379584612146723589258961734
947635218683241597125897634712459386594386721836172945278964153351728469469513872
359872146278641539614359872732164985146985327985237614867493251423516798591728463
397815642562497183184623975249358761835176429716942538453269817921784356678531294
917283645354671829862495371429816537586734912173952468231549786745168293698327154
691538472835247619427196583589614237273859164146372895758921346912463758364785921
831265974476819532259374816384192657567438129192756348615927483928543761743681295
875963241961482357243571698426798513197635482538124976319257864752846139684319725
365729481241856379798143526579681234123475698486932157812594763954367812637218945
597312864418567392326498175973251648684973521152684937239145786761829453845736219
752836941683491527941752638829145376514673892376289154437968215298517463165324789
687253194421978653593164782816549327235781946749326815168435279374892561952617438
813952647647381529925764831279615384584239176136478295391846752752193468468527913
352918674489736125617425938824371596573869241961254783745682319138597462296143857
216738954974215638358964172821453769439176285567829341793542816685391427142687593
641587329389214567527963841856791234192345678734826915915672483273458196468139752
284735196379162458516489327158397642962854713437216985645978231793521864821643579
278435691519682347463971528347269815851347962692518734726153489984726153135894276
149627853365189247728543196481372569596418732237956418974261385853794621612835974
168279453259143876473685219946851732817432695325796148632917584794528361581364927
216849735753621894489753216832596471947138562561274983174965328695382147328417659
142896537378215649659374182826941375917583426534627891293158764461732958785469213
574962318962318457183754269896147523235896741741235896317429685628571934459683172
473261895298345617561987342952418736184673529736529184845196273619732458327854961
873215649249678531651394287514923876386547912927186453432861795168759324795432168
513429678678531924492678153859362417721954386364817592147296835936785241285143769
741835269269174358835629741574912683398467125126583497483756912912348576657291834
269854371518732496374196852921685734843279615756413289132568947685947123497321568
876345219925187634341926578453618927682739145197452863239871456718564392564293781
863917425129845367754632819487329651392561784615784932931276548276458193548193276
326978541145263879978415236783594612462381957519627483894132765251746398637859124
394675812275841936861239547137492658542768391689513274756984123423156789918327465
925783614784961253136245789893657142562194378417328596359876421678412935241539867
429871536361245879587369142973186425245793618618452397732518964156924783894637251
821975436597346218634128795452839167983761524716254983269487351375612849148593672
165842973284397651739561482673984125842175369591623847357416298428739516916258734
418963527362758491579412836783124659295637184641895273954386712127549368836271945
152789436976534812834216759589461327723958641461327985298645173317892564645173298
971364285528179346463285917349721658217658439856493172185942763694837521732516894
594712638673498521281653479417825963825936147936174852349261785162587394758349216
651834927479512368328769415135928674746153289892476531967385142214697853583241796
963714852247859631851326749526493187739185426184672593375968214698241375412537968
512347968743698521689251437137564289456982713298713645871425396364879152925136874
986325714714986253325471698632149587849752136157863942573298461298614375461537829
682371945497265183351984627516492378749538216823716594238157469964823751175649832
365712489412859637789643152691574823574238916823196745247361598936485271158927364
618435792932718654574962381467293815293581467851647239789126543345879126126354978
286753149735194682941628375198475263623981754574236891857319426419862537362547918
276814395189536274453729681562183947794652138318497562631278459845961723927345816
815649723469372158732851694693785412248196375157423986521964837974538261386217549
359647812768219543214853679873921465921564738645378921582736194496182357137495286
796528314842137695135694287954783162261459873387261549673842951428915736519376428
569287134371495628248631597826549371415763289793812456954128763637954812182376945
943827165561394872827615394286531947739482516154769238418956723695273481372148659
874932516639154278215768943943271685586493127721586439392647851158329764467815392
518972643364851972927643581789526134156437829243189765632715498495268317871394256
395827164681534792274916853427358916853169427916742538162485379549273681738691245
871594362493672815562183497384917526156248739729356184615439278247861953938725641
851437692734629581629851473468572139215983746973164825346795218597218364182346957
469753218735218694812694573591326487374589126628147935247861359186935742953472861
156932874948571362372846591721394658695218743834657219413725986569183427287469135
592476138813925674674831925761382459459617382328549761135264897246798513987153246
423758916179623458658491237541879362392516784867342195235167849984235671716984523
185923647739416528642578319916852734473691285528347196397185462264739851851264973
278653419153948672469721583395472168814369725726815934631584297587296341942137856
874631592631592847592874613253149786467283159189756324928365471345917268716428935
542938617176254839389761425261479358753816942498523176624387591915642783837195264
981725634327496581564381279436579812872614953159238467215963748693847125748152396
371695248659284317248137659983512476524876193167943582715328964492761835836459721
147598362295163478386427519569381247423679851871245693618952734734816925952734186
241935678786142539593678142935781264817426395462593781629817453154369827378254916
296341758143785692875692341462517839938264517517839264329476185781953426654128973
748315269965872134231946578523789416197564382684123957812457693459638721376291845
978362541145789632263415798514927863796834215832651479481296357357148926629573184
145239768896475132732618945328164579957823614461597283573981426219346857684752391
652431897973258416148697532539762148214983765786145923861379254425816379397524681
327658194568149327941273586692517843715834962483962715876495231159326478234781659
243715986851964732796238514912853467365497821478621359627389145189546273534172698
368915724519724368724836591872569143653148972941273685196452837485397216237681459
256984731987631245341257869523178496469523187178496352794815623815362974632749518
126954378458673921739218456672395814915487632843162795384721569561839247297546183
597823641286514739314697528172946853648352197953781264465138972731269485829475316
468215397321879654795643821954321768682457913137968542513794286279186435846532179
713946285954218637628753419365487192847129356291365874176894523489532761532671948
825619743916743852473528916759132468642875391138964527591287634367451289284396175
659318247872456931143279586798562314524831679316947852965184723437625198281793465
198325674623794158754681239319847526265139487847256913972413865431568792586972341
716439285394285176825167934269374851473851629158926743542698317687513492931742568
841953627359762841762814935634581792985427163127396584493675218278139456516248379
291745386386291475547386912473518269815962734962473158154827693728639541639154827
742539816519862473638417952475283691196754238823691547251346789987125364364978125
396425178247819356185673429634587291758192634912346587479231865521968743863754912
951267438374518629862349157598421376617935842243786915126854793785193264439672581
167293845893514762425687193736142958518369427249758631971425386354876219682931574
921356478385174926476982531214567893863419257597238614658793142132645789749821365
821369547547218639936475281762531894153894762498627315374156928619782453285943176
756843192943521768128679354875936421631284975294715683362157849517498236489362517
781493562954612783263758194438167925125389476697524318812945637579236841346871259
697148235143257968258369147376591482519482376824673519435726891962814753781935624
952431876378652149461789532719368254245917368836245791193876425524193687687524913
719482365635917284824635197196528743347169528582374916471893652268751439953246871
215736498936482175748591236891324657567918342423675981382147569154869723679253814
613725489275498361849163257932617548584932176761584932426379815158246793397851624
256174938714983562389526417561842379892357641437691285623715894975438126148269753
821957634647832159395146287572369841963481572418275963136524798254798316789613425
987524316452361798136897425365489172821673954794152683619235847273948561548716239
921648573846357192375291864593874621162539487784162359239485716418726935657913248
523681794819745236764329851982137465371456928456298317247513689138964572695872143
568193427174825396923476158712648935635719842489352671897264513246531789351987264
612798534879354162345612978584976213231485796967123845756849321498231657123567489
423571689689432157517869324261943875395287461748156932154628793976315248832794516
316278594874159326592463781158792643467381952239645178721534869683927415945816237
947328615325619487186547923514763298673982541298451376762895134431276859859134762
945317268173628594286459137527943681314286975698175342459861723732594816861732459
216873495378594621594126378132459786459687213687312954965741832741238569823965147
627591348198243576534867219856724931419385627273916854985472163341658792762139485
285417396967325814143986527621573948839264751574198263496732185318659472752841639
254678391913425867678913254341789625789256413562134978136897542425361789897542136
823514796415967823769832145246753981537189462981426357378295614154678239692341578
395762418418593762627841953281659374956437821734218695849175236172386549563924187
359168742724395861186274593432689157571432986968517234647951328215843679893726415
412897635365421879798536412629354187543178296187269543951683724274915368836742951
413529678987634152652781394739812465546973281128456739261398547395247816874165923
179463258648925173253187649482351796531679482967248315396514827815732964724896531
249176358675398421138425976917632584854719632362584197521843769796251843483967215
681254397942783615573961284416839752358627941729415863167348529295176438834592176
386457291574192368921386754163875429249613587758924613697541832832769145415238976
256734918487192653193865427372941865914658732865273149629517384748326591531489276
751392846436581729982746513817235694594618372263479185679823451145967238328154967
758429361412836957396715284183542796675198423249673815564987132937261548821354679
694183572813752496257946183176834925485629731329517648532491867961278354748365219
927568134854319267136427985582943671671285349349176852498731526265894713713652498
275984613948136275316257894127563948583492167469871352654329781892715436731648529
814923756796154823235867914459386271172549638683712495328475169547691382961238547
813659274274138596695247813156723489932481657487965132361594728728316945549872361
349827561615439827728516439153678294962154783487293615836741952571982346294365178
439268751862715943715349862381697425524183697976524318653472189197856234248931576
412537869963184527785296431156872394827943156394651782548729613679315248231468975
324867519587192463691543872162359748953478126748216395819725634436981257275634981
978165324526374981134289576843751269715692843692843157457938612361527498289416735
967583241435261987812749635796135824583624719124978356251397468349816572678452193
892571346457263981361948725523614879176892534984735612618457293735129468249386157
947351826286794351351826974895162743734589612612473589179235468468917235523648197
972635481536841927184927365498216573263574198751398246619483752827159634345762819
245967138396184527718352946457629813839741265162835479624578391571493682983216754
368592471475183692129467385742956813596831724813724569937615248651248937284379156
321856947749132685658479213875914362436725891912683574567391428193248756284567139
751264398389517246642983157196425783425738961873196524234679815518342679967851432
293518746476932518851674293512496837964387125387251469745163982628749351139825674
247385961863921547951764382372196854685432179194857623518249736439678215726513498
147829536362514897958367142283956714714238659695471328821643975436795281579182463
932864571158729463647135928273941856586372149491658237865293714329417685714586392
695438712271695438843127659486912375537846291129573864752389146364251987918764523
638925417529147683147863592215479368974386251386512749861234975453791826792658134
617593842942867513358124796429718365536942178871356924293481657765239481184675239
962843715438517926175296348381925467746138259259674183517362894894751632623489571
379468152281795346456132798928647531647351289135829467713984625594216873862573914
938726541672145893154938726387562419419387652265491378526879134841253967793614285
975361248462875319138429657627538491351942876849716523513287964286194735794653182
952731648741682359638945127186324795324579816579168432465893271217456983893217564
126754389398612547754398216679521438543867921281943675862135794415279863937486152
248561739593247861167893254916432578324758196785916423651324987832179645479685312
943857612862941753571236984486725139139684527257319846395162478724598361618473295
781649325235817469946352871193426587628175934574938216359781642467293158812564793
198756234276438951435129786962384517751962348843517629527641893684293175319875462
185439627693257148247816593469385712358721964721694835814563279536972481972148356
568439712917285463423617598134752986896341257275896134752168349649523871381974625
645213798813976452297845613738159264461782539529634871152497386974368125386521947
967415823214389567538267491496153782375928614821746935159872346643591278782634159
267915348195348267834627915572891634918436572643572891426153789789264153351789426
813645279465729183927831456581296347732458961694317528348162795156974832279583614
927643815436518792158927436579164283641382957382759164764831529893275641215496378
594231876321876954687495132478519263915362748263784591736158429152943687849627315
217836495683954217549712386458169732721543968936287154894375621162498573375621849
587246139634891275912735846859673412421958367376124958748362591195487623263519784
763924851185637429942158763237596184418372596596841372354289617821763945679415238
473856192569421783821739456298374615734615928615982347356198274187243569942567831
137526984694387215825149367316492578479815632258763491942671853783954126561238749
652947318497381625831652947289174563174536289365298174928465731713829456546713892
851632947623974185497158623186547239932861574574293816245786391768319452319425768
378251694912674538645983127834197265297568341561432789729345816186729453453816972
178296534962354178543817629429735816681429753735681942297163485854972361316548297
719562843265438179843917652198274536472653918356891724937146285624785391581329467
693274581428165397715938624549623718187549263362781459856497132234816975971352846
673942158912578346485163792298431567764895213351627489526319874139784625847256931
256491738471238569893765421534876192629143875718529643945387216162954387387612954
491736582376582941285491376517269438834157629962348715149875263623914857758623194
562719834897453612341862759259381476674295381183674295718946523936527148425138967
258413967143967852796258134815376429962541378437829516374695281689132745521784693
435179826917286354628354971241937568596418732873625149169743285382561497754892613
385692741947183265162754893279861354518347926436925187891576432623418579754239618
746395821521847936893261457234586179179432685658719342462978513315624798987153264
925741386467938125813625947194356872672894513538172469751463298289517634346289751
458763912627819345913425876842637159391582467765941283289156734574398621136274598
519847623237916485864352719651239847478165392923784156342578961196423578785691234
925614378734298615816735924479582136158963247263147859642359781597821463381476592
894251736251736948736489251419827563368915427572643819923568174685174392147392685
361582479258794613974631582513927846896345721742168935189453267627819354435276198
581643297392785416674219538138927654465831972927456381849372165716594823253168749
267519438915843726384627159152964873736281594498735261571398642823456917649172385
731826495945371826682459173874693251169582734253147968398715642517264389426938517
175489623623157849498362175254713986986245731317698452832976514761534298549821367
638251479147869532952347816215634987789125364463978125576483291394712658821596743
465187293793625148218934756937251684846793521521468937654372819189546372372819465
718243659542967138369815247951638472427159386836724591293471865174586923685392714
358942617729561384641837592865723941934158276172496853287619435593274168416385729
619723458352849167874651329261935784593487216487162935936514872725398641148276593
283617495496582317715934826349258761572146938861379254638795142957421683124863579
127435968354689271698712534912347685586291743743856129875963412239174856461528397
215698734437521896968374512186745329392186457754932681623817945549263178871459263
761984532328715496459263187875492613613578924942631758137849265594326871286157349
594782163827136945631954278352698714418527639976341582263819457745263891189475326
231849675957326148648751239786914523194532786523687914475268391319475862862193457
693458217174923685582167394469271538217835946358649172726394851941582763835716429
928471563147356982635289714791562348483197625256834197879645231514923876362718459
932867145768514239514932876643728951287195364195643728351479682479286513826351497
587319462162458937934672851619825743453796128728143596896531274345287619271964385
576321984413859627289476351394265718827194536165783492632948175948517263751632849
674258931852913746391647285429186357537492168168375429983521674215764893746839512
246785913319264587587391246493812765765943821821576394172439658658127439934658172
435921687978653124612748539249386715157294368863175492591867243786432951324519876
832615974947283651561794283418937562753826149629451837275369418396148725184572396
982136754364597182571842396856724913193658247427319568749285631235461879618973425
431269578925781643867453129248536791653197284719842365186925437374618952592374816
254176983197283654683594712712639845546812397839457261925361478361748529478925136
436781592278539164915246387561374928892165743743892651354918276627453819189627435
913472568658931742472586139295163874361748295847295316784329651536814927129657483
687195234143682579952734816798356142435271698216948357364529781529817463871463925
213498657874561329596237148462185793759643812138972465627819534981354276345726981
453291768962387145187654239379512486546978312821436597615749823794823651238165974
862359714593174826471862359327685491914237568658491237286713945745926183139548672
427651983358947621961382574746135298289764135135298746593426817674819352812573469
763249185425138769891657342149823657576914238382576914218395476957461823634782591
813269574495378612672451938586124793937685241241793865129836457754912386368547129
948173526612845973735269481561497832824631759397528614456712398189354267273986145
746953812539812647821467935154738269268591374397624158482376591973185426615249783
691283745547169832283547961814735296375926184962418573728354619139672458456891327
751649238283175964649823571428396715396517482517482693162934857875261349934758126
635429781489317256712586943897241365326875419154963872948652137573198624261734598
734128695596347128821659374165293847983714562472865913259436781318972456647581239
186794532352681974974235618423519786519876243768423159895142367241367895637958421
357248619619537824284619375491862753862753941573194286138925467925476138746381592
597268413682314957413579862835196274961742538724853691349627185258931746176485329
694378125372519846581624937138795462927146358465283719259437681713862594846951273
958643172723185964416972583549831627831726459267594318375418296692357841184269735
354172869129468753768935421297543186685217394413689572842356917971824635536791248
215739864973468125684215739458697213796321548132854697549182376327546981861973452
283169754475832916961754238528397641614285379739641582156423897342978165897516423
348719652719265483562348197497683521683152974251497836926874315135926748874531269
845762193291534876673918524916275438384196257527843961769421385452387619138659742
593142768427968135618537249235671984176489352984253671752394816349816527861725493
458976123971243856362815974723168549594732618186459237235687491817594362649321785
927186543546932178381574962269458317713629854458317629834761295192845736675293481
864375192357129648291486573129638457483517269576294831638751924715942386942863715
127683459638594217549172863263417985481359672795268341916835724354726198872941536
973524816258619347614873925431296758829457631765381492597148263382965174146732589
169582374287349561435671892392165487518734629746928153821457936654293718973816245
275438196436195728198762453319247685567981234824356971981623547743519862652874319
532167894918245637764983152421358976853796241679421583145872369396514728287639415
368124759975386214214759836536497128149238675827561493753842961492615387681973542
291685347685473921437219865128734659543926178769158234314592786952867413876341592
795831246624957138183462579317285694542796381968143752851324967476519823239678415
234986517715234689698157432586342971341798256972615348163579824827463195459821763
786249351135687249924135786359861427261574938847392615678453192492718563513926874
368524791927613548415798236839147652652839417174265983791486325583972164246351879
865913427319472586274586913458267139193854762726139845642798351537641298981325674
516829734289374615374165892637498251152736948498251376865917423921643587743582169
967483125583127649421659738138296574745318962692745381354972816279861453816534297
159246387264837951783951264376584129428169735915723846841375692537692418692418573
635487921291563784847219365764128593182395647953674812318952476476831259529746138
793546128182379456465128973621485739879213645354967281517632894236894517948751362
349286157712954368856173924287349615493561872561728493174892536928635741635417289
597213846284596317316847529923651784748932165651784293465178932172369458839425671
482695317317842596956713284134986752879254163265137948728569431541378629693421875
351278649964531728287496513842769351796153482513842976179384265625917834438625197
657928431892134756431675298275346189918257364364819527583761942149582673726493815
741362958589741632362958741936827514154639287827514369273486195495173826618295473
358471629427963158691285347569738214142596783873124596915647832734852961286319475
941526378375841926268793451432965817689217534517438692726389145194652783853174269
714256983839714265625398471381425796257169348946837152462981537198573624573642819
615372849734891526982465731468237195159684273273159468897526314346718952521943687
389745162745612893261839754517428639493567218826391547654283971138976425972154386
918245367523876491674193852136582974789614523245739618351928746892467135467351289
752364819894715623136289475921643587643857192587921364368592741479138256215476938
658413297914762853372985614187234569569871432423596178746358921831629745295147386
418596732569237184732481659627349518145728396893615247284173965376954821951862473
573841962814269573926357814459726138367185429182934756231478695698512347745693281
251867943674932851839415726568724139913658472742391568325179684497286315186543297
428376519196452378537918624342769851851234796769185432973641285615827943284593167
851239746293647518764815293918753624426198357375462189187324965649571832532986471
514879632263451897789362514976528341431697258852134769145786923628943175397215486
879613425524798163163425798791536842458172639236849571682357914915264387347981256
184967523769523418352184697876459231493218765521736984935671842248395176617842359
465879231327154698189362547543618972672495183891723456916537824758241369234986715
416897523729351684385264917942683751571942368638715249163578492857429136294136875
415273698879641253236859174627538941384916725591427386762184539158392467943765812
581642739674931825932758416849215673215367984367489251196823547723594168458176392
689175432523469871147238965458917326791623584236854719865341297972586143314792658
156798324438625917279314685392456871541987263867132549723561498984273156615849732
319872564287564193645193278598721346462385719173946852856219437921437685734658921
918673542257894163436152789794385216583261497621947358365719824179428635842536971
286513479514697238397248165825769341479321856631485927963152784748936512152874693
854126937732495186916783452148357629295861743673249518329614875581972364467538291
138462597527983641946751832874319265692845173315627489269574318781236954453198726
319562784652478319487931526823745691961283457745196832178659243234817965596324178
659843271483127596127569834748391652316254987295678143571932468864715329932486715
519683274734129865682457319928514637157236948463798152275961483341872596896345721
489263715715489326362571489596712843273894561841356297154627938627938154938145672
716248935248359617953671824392584761571936248864712359139427586427865193685193472
781293456932654718465817392326978541548136927179425863814769235657342189293581674
381694752257831964649572813724916538835427196196385247963258471512743689478169325
783549126126738954594621378618972543245386719379154682952867431431295867867413295
514287693693154872728396514156739248247618359839425761362541987485972136971863425
657483291283159746194672385729514863465328917831796452518937624976245138342861579
132874695965132487784956132613289754249517863857643921576428319328791546491365278
492875316875163924136294758984527631527316489613948275268431597341759862759682143
546297318183456729972318645394761582617825934825934167438179256761582493259643871
436972581815364279729815346942756138381249765657138924164523897593487612278691453
713928654564371829289465173675142398938657241421893765197586432856234917342719586
763924851925187634148563279284316597316759482579248163457632918831495726692871345
297341658684275139531689724319468572725913846468752391956827413143596287872134965
129478356654392718387156492872615934913847625465239187236984571741523869598761243
249683175368571249157942863892417356635829417714365982971254638483796521526138794
179258436852634971364179852296817543548963217731425689427386195915742368683591724
746892315852314697139675428583961742274583961961427583328746159497158236615239874
731489562852167943946253187193825674674391258528674319287916435315742896469538721
164278953972534861358196472427961538836752194591483726289615347615347289743829615
627584391854391267391726548419673825736258914582419736165937482243865179978142653
673192485251483976894576213945327861782651394316948752429865137168734529537219648
158967423342815769679432581963741852815326947724598136286174395431659278597283614
354216897987534612621978345718345926263891754549627138832759461196482573475163289
791364825436825917582917364367248591259671438814539672943152786625783149178496253
913246785248537196567198342795324618186975423324681579831452967452769831679813254
456973821218456973379218465587692134692341587134785692765834219921567348843129756
724639185963851427158472936386145792219763548475298613897316254631524879542987361
589164372362597184174283596897431265643852917251976438725318649938645721416729853
138762594524391867697854213812637459946518732753249186361425978275983641489176325
841769325763245891925138746214873659586491273379652184438517962692384517157926438
425618937673249815891537642184376529236495781759182364947823156362751498518964273
347685192265791834198324576816253749953467218724819365672148953581936427439572681
329745618857162439416938275742619853538274961691853742273596184965481327184327596
318427569467591238952836714876354192241968357593712486184675923735289641629143875
163487592547692183982315764871243659634958271295176438359724816418569327726831945
831549762276318495459267318918753624764182539325496187593871246187624953642935871
527913684341685279698724531853279146164538792972146358786451923415392867239867415
258367941367914852914825367432679185796581234185243796623158479579432618841796523
