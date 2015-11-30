import string
import re
import math
import nltk
from nltk.corpus import cmudict

#ntlk.download() #Uncomment this line the first time you run and download the cmudict, used for iambic pentmeter

validWords = ["understandings","understanding","conversations","disappearing","informations","grandmothers","grandfathers","questionings","conversation","information","approaching","understands","immediately","positioning","questioning","grandmother","travellings","questioners","recognizing","recognizers","televisions","remembering","rememberers","expressions","discovering","disappeared","interesting","grandfather","straightest","controllers","controlling","considering","remembered","cigarettes","companying","completely","spreadings","considered","continuing","controlled","stationing","controller","straighter","stretching","businesses","somebodies","soldiering","countering","darknesses","situations","directions","disappears","younglings","suggesting","afternoons","breathings","distancing","screenings","schoolings","especially","everything","everywhere","explaining","explainers","expression","branchings","revealings","repeatings","surprising","rememberer","somewheres","television","themselves","recognizer","recognizes","recognized","belongings","finishings","travelling","questioner","beginnings","travelings","questioned","followings","pretending","forgetting","forgetters","forwarding","positioned","travellers","gatherings","perfecting","understand","understood","weightings","approaches","officering","numberings","happenings","mentioning","letterings","husbanding","imaginings","approached","apartments","whispering","interested","discovered","spinnings","clearings","climbings","spendings","clothings","colorings","soundings","truckings","somewhere","troubling","companies","companied","beautiful","computers","confusing","considers","travelers","youngling","continues","continued","traveller","traveling","yellowing","apartment","beginning","wheelings","travelled","sometimes","something","appearing","cornering","believing","countered","believers","countries","soldiered","coverings","creatures","crossings","accepting","daughters","belonging","situation","silvering","different","silencing","touchings","bettering","tomorrows","disappear","thinkings","boardings","discovers","admitting","wrappings","distances","distanced","sightings","shrugging","doctoring","showering","shoulders","shoppings","shootings","dressings","sheetings","shadowing","settlings","servicing","seriously","seconding","searching","weighting","screening","screaming","schooling","teachings","bothering","everybody","botherers","bottoming","excepting","expecting","explained","direction","explainer","surprised","surprises","waterings","branching","revealing","returning","surfacing","familiars","repeating","fathering","reminding","supposing","breasting","attacking","remembers","breathing","remaining","breathers","brightest","brownings","suggested","recognize","fightings","attention","figurings","receiving","reasoning","realizing","fingering","buildings","finishing","stupidest","stuffings","questions","watchings","flashings","strongest","strikings","flighting","flowering","promisers","promising","following","bathrooms","prettiest","pretended","stretched","foreheads","foresting","stretches","forgotten","pressings","forgetter","strangest","preparing","forwarded","strangers","possibles","positions","afternoon","straights","pocketing","gardening","pleasings","wondering","gathering","picturing","personals","perfected","stomaches","stomached","carefully","stationed","catchings","parenting","paintings","orderings","groupings","wintering","officered","offerings","centering","numbering","neighbors","certainly","happening","narrowing","narrowest","mountains","mothering","mirroring","middlings","messaging","standings","mentioned","mattering","marriages","histories","machining","hospitals","listening","lightings","springing","lettering","husbanded","spreaders","whispered","imagining","imaginers","spreading","important","languages","answering","cigarette","interests","spiriting","cleanings","knockings","soundest","coatings","sounders","sounding","colleges","coloring","colorful","wouldn't","training","colorers","sorriest","worrying","belonged","approach","tracking","touchers","touching","computer","whatever","toppings","confused","confuses","workings","consider","bettered","teething","tonights","tonguers","tonguing","continue","arriving","tomorrow","controls","together","blacking","blackest","throwers","blocking","throwing","coolings","someones","blockers","somebody","thirties","soldiers","cornered","weighted","counting","thoughts","counters","thinking","thinners","thinning","coursing","covering","thinnest","craziest","snapping","creating","creature","thickest","boarding","crossing","smokings","crowding","smelling","smallest","cuttings","slipping","slightly","dancings","sleepers","sleeping","slamming","wordings","darkness","daughter","boatings","skinning","weddings","thanking","sittings","deciding","deciders","singling","singings","despites","simplest","terrible","silvered","tellings","wearings","youngest","watering","silences","teachers","bookings","agreeing","teaching","discover","attacked","bothered","botherer","watching","swingers","bottling","distance","silenced","signings","bottomed","sighting","shutting","shrugged","wondered","swinging","doctored","sweetest","showered","showings","doorways","shouting","shoulder","wronging","shortest","surprise","dragging","shopping","shooters","drawings","actually","shooting","dreaming","dressing","avoiding","shitting","shirting","shipping","drinking","drinkers","braining","sheeting","sharpest","drivings","sharpers","dropping","droppers","shadowed","surfaced","settling","washings","settings","services","serviced","earliest","backings","earthing","servings","branches","branched","seconded","seatings","surfaces","searched","searches","walkings","screened","waitings","screamed","supposed","emptiest","emptying","breaking","breakers","schooled","enjoying","enjoyers","entering","runnings","breasted","rounders","rounding","supposes","everyone","visitors","visiting","breathed","excepted","roofings","exciting","breathes","expected","rollings","bankings","breather","explains","villages","bridging","viewings","brighter","ringings","righting","suitings","bringing","revealed","bringers","returned","failings","repliers","replying","repeated","brothers","familiar","wintered","families","suggests","farthest","furthest","browning","fathered","removing","building","reminded","bathroom","allowing","suddenly","remember","allowers","feedings","builders","burnings","feelings","remained","refusing","stupider","windings","although","stuffing","studying","business","angriest","fighting","fighters","students","figuring","received","twenties","receives","fillings","reasoned","findings","stronger","turnings","realizes","realized","readiest","fingered","readying","striking","trusters","finishes","trusting","finished","readings","reachers","reaching","quieters","quietest","quieting","fittings","quickest","writings","beaching","question","trucking","callings","stranger","flashing","beatings","answered","flattest","flatting","flighted","straight","troubled","flowered","pullings","storming","promiser","couldn't","promised","promises","couldn't","followed","stoppers","problems","probably","prettier","stopping","pretends","stomachs","troubles","pressers","tripping","forehead","stickers","forested","pressing","whispers","carrying","sticking","carriers","stepping","stealers","forwards","stealing","becoming","prepares","prepared","powering","freeings","stations","possible","position","freshest","beddings","wrapping","fronting","catching","fuckings","policing","funniest","pointers","pointing","catchers","pocketed","gardened","starters","ceilings","pleasing","gathered","starting","centered","platings","plastics","planning","pictured","pictures","traveler","pickings","personal","glancing","yourself","chancing","perfects","changing","peopling","partying","partings","parented","grabbing","grabbers","changers","checking","starring","bedrooms","checkers","pairings","standing","painting","outsides","greatest","cheeking","greening","greenest","grouping","ordering","anything","openings","guarding","wheeling","officers","guessing","spreader","offering","children","anywhere","numbered","choicest","noticers","noticing","hallways","nothings","hangings","nobodies","admitted","neighbor","choosing","choosers","happened","neckings","happiest","narrowed","narrower","spotting","churches","mouthing","traveled","mountain","mothered","accepted","mornings","mirrored","headings","spirited","hearings","heatings","circling","middling","messaged","messages","heaviest","wouldn't","spinners","mentions","helpings","cleanest","memories","meetings","meanings","appeared","mattered","marrieds","marrying","marriage","yellowed","markings","cleaning","managing","cleaners","holdings","machined","machines","lunching","luckiest","lowering","longings","clearest","hospital","lockings","littlest","clearing","listened","housings","lightest","lighting","lighters","spinning","hundreds","hurrying","believes","spenders","believed","climbing","husbands","lettered","lettings","learning","leadings","ignoring","laughing","ignorers","imagines","yellower","imagined","climbers","imaginer","spending","closings","specials","speakers","language","believer","clothing","clouding","speaking","interest","spacings","landings","knowings","southest","jacketed","knocking","kitchens","kissings","killings","keepings","dresses","biggest","sticker","careful","shirted","warmers","shipped","birding","drinker","carries","sheeted","warming","carried","carrier","driving","sharper","tonight","drivers","casings","sharers","sharing","stepped","dropped","dropper","whisper","shapers","shaping","shakers","shaking","tonguer","shadows","stealer","several","tongued","staying","settles","settled","dusting","setting","tongues","catting","backing","catches","earlier","warmest","earthed","service","serving","warring","wanters","catcher","serious","eastest","sensing","senders","easiest","sending","sellers","selling","seeming","seeings","tiniest","seconds","station","causing","seating","edgings","stating","timings","efforts","starter","causers","screens","blacker","ceiling","screams","centers","wanting","walling","walkers","certain","emptied","empties","emptier","thrower","endings","started","schools","scarers","scaring","sayings","engines","savings","sanding","enjoyed","starers","saddest","enjoyer","staring","enoughs","rushing","bagging","runners","entered","running","chances","entires","chancer","rubbing","rowings","rounder","chanced","rounded","starred","rooming","changed","changes","blocked","angrier","exactly","changer","blocker","excepts","checked","excited","walking","excites","roofing","through","expects","blooded","checker","cheeked","throats","explain","wakings","springs","thought","waiting","blowing","rolling","rocking","risings","ringing","baggers","animals","righter","righted","ridings","richest","facings","reveals","blowers","choicer","choices","returns","voicing","worries","resting","chooses","failing","spreads","replier","failers","falling","spotted","replies","replied","chooser","thinned","fallers","thinner","balling","boarded","repeats","visitor","farther","further","circles","another","removed","fastest","removes","fathers","thicker","circled","visited","reminds","fearing","spirits","classes","answers","banking","boating","cleaned","feeding","spinner","thanked","village","worried","feeling","cleaner","remains","cleared","refuses","refused","workers","reddest","telling","yellows","spender","working","clearer","clearly","climbed","tearing","fighter","teaming","figured","figures","booking","viewing","climber","usually","closest","receive","filling","teacher","reasons","closing","finally","closers","anybody","finding","anymore","realize","special","finders","booting","realest","clothed","readier","readies","readied","fingers","teaches","tallest","clothes","speaker","readers","talkers","clouded","talking","reading","firings","spacing","takings","reacher","reached","coating","reaches","raising","raining","fishing","quietly","fittest","fitting","systems","whether","bothers","wrapped","fitters","quieted","quieter","quickly","coffees","quicker","fixings","coldest","sounded","sounder","actings","anyways","college","flashed","flashes","bottles","flatter","flatted","colored","bottled","wording","turning","sorting","flights","colorer","putting","pushers","pushing","flowers","pullers","swinger","wonders","sorrier","pulling","proving","comings","bottoms","promise","truster","boxings","company","follows","younger","trusted","sweeter","yelling","problem","without","beached","footing","confuse","beaches","brained","bearing","pretend","trucked","forcing","presser","wishing","trouble","forests","appears","beating","airings","forever","surface","control","forgets","accepts","pressed","wronged","winters","forming","presses","prepare","beaters","breaker","wheeled","because","forward","coolers","cooling","allowed","powered","pourers","freeing","pouring","tripped","coolest","breasts","someone","fresher","suppose","somehow","friends","breaths","copping","fronted","becomes","porches","poppers","popping","poorest","treeing","fucking","fullest","pooling","breathe","polices","funnier","funnies","policed","bedding","corners","futures","pointer","pointed","gamings","counted","soldier","pockets","wetting","pleased","gardens","wetters","wettest","pleases","counter","sunning","players","westest","country","gathers","bridges","playing","plating","bridged","plastic","couples","softest","getting","planned","getters","placing","gifting","pinking","pilings","piecing","picture","coursed","courses","summers","picking","snowing","phoning","bedroom","glances","glanced","winging","snapped","glassed","glasses","perhaps","covered","crazies","crazier","perfect","peopled","persons","peoples","suiting","pausing","passing","goldest","partied","windows","parties","parting","creates","grabbed","smokers","created","grabber","brought","weights","bringer","arrives","crosser","crosses","grasses","parents","palming","graying","pairing","crossed","painted","arrived","greying","smoking","paining","outside","brother","greater","smilers","outings","greened","greener","crowded","travels","smiling","ordered","grounds","offings","smelled","openers","browner","grouped","opening","smaller","growing","okaying","officer","guarded","slowest","slowing","cupping","slipped","guessed","guesses","cutting","offices","gunning","offered","browned","allower","nursing","numbing","suggest","cutters","numbers","sliders","halving","sliding","noticer","wedding","notices","noticed","nothing","writers","hallway","handing","sleeper","normals","noising","hanging","nodding","dancing","wearing","writing","slammed","hangers","darkest","skinned","happens","trained","needing","builder","beliefs","happier","necking","nearest","hardest","nearing","burning","believe","winding","hatting","narrows","stupids","sitting","mouthed","deadest","watered","sisters","mothers","singled","winning","morning","mooning","moments","heading","missing","decides","decided","decider","mirrors","minutes","hearing","minings","already","minding","middled","heating","burners","singles","middles","deepest","stuffed","heaters","singing","simpler","heavier","heavies","belongs","message","despite","mention","simples","studies","studied","silvers","helping","helpers","members","meeting","willing","meanest","attacks","herself","meaning","dinners","student","hidings","matters","marries","married","busying","busiest","silence","against","highest","wildest","hilling","marking","mapping","manages","managed","himself","history","tracked","strikes","manning","hitting","makings","hitters","whiting","towards","watched","holding","toucher","machine","holders","lunches","lunched","watches","luckier","stretch","streets","lowered","loudest","lookers","looking","longing","calling","longest","locking","bending","washing","signing","hottest","littler","benders","strange","sighted","listens","linings","likings","housing","beneath","sighing","sicking","however","lighted","sickest","lighter","calming","lifters","hundred","calmest","hurried","hurries","lifting","touched","doesn't","doesn't","hurting","touches","showers","husband","doctors","letters","cameras","letting","tossing","leaving","learned","dogging","leaning","leafing","leaders","leading","whitest","layered","ignored","showing","ignores","stories","ignorer","shoving","laughed","lasting","largest","imaging","doorway","besting","imagine","shouted","stormed","downing","storing","topping","avoided","dragged","shorter","betters","stopper","landers","insides","instead","written","drawing","shopped","stopped","between","landing","shooter","knowing","jackets","dreamed","carding","toothed","knocked","knifing","kitchen","joining","teethed","stomach","joiners","kissing","kindest","killers","killing","shoeing","kidding","jumping","kickers","kicking","jumpers","keepers","dressed","keeping","enough","checks","kicked","jumper","kicker","kidded","jumped","killed","joking","killer","kinder","joiner","kisses","kissed","joined","knives","knifes","knifed","jacket","knocks","itself","ladies","landed","lander","inside","larger","images","lasted","imaged","laughs","ignore","aboves","laying","accept","layers","across","yellow","leaded","leader","leaved","leaned","learns","leaves","yelled","lesser","letter","living","lifted","lifter","humans","hugest","lights","wrongs","houses","liking","likers","lining","housed","acting","listen","hotels","little","hotter","locals","locked","horses","longer","longed","looked","hoping","looker","losing","adding","louder","loving","lovers","lowing","lowest","writer","lowers","homing","holing","holder","making","hitter","makers","manned","manage","writes","admits","mapped","marked","hilled","higher","afraid","hiding","hidden","matter","ageing","helper","member","helped","memory","hellos","heater","metals","middle","heated","mights","minded","hearts","mining","minute","headed","mirror","misses","missed","moment","moneys","monies","months","mooned","mostly","having","mother","worlds","hating","mouths","moving","movers","movies","musics","worker","myself","naming","namers","narrow","hatted","hardly","nearer","neared","nearly","harder","necked","needed","happen","hanger","newest","nicest","nights","worked","nobody","nodded","handed","noises","noised","worded","normal","norths","nosing","agrees","noting","notice","halves","halved","number","guying","numbed","nurses","nursed","agreed","wooden","offing","gunned","offers","office","guards","wonder","okayed","okay'd","okay'd","ok'ing","ok'ing","oldest","womens","opened","opener","groups","womans","within","ground","orders","others","outing","wished","greens","greats","owning","wishes","owners","paging","pained","paints","greyed","greyer","paired","palest","grayed","palmed","papers","grayer","parent","parted","passed","golder","passes","pauses","paused","paying","person","people","wipers","goings","glance","phones","phoned","photos","picked","giving","givens","pieces","pieced","piling","gifted","pinked","pinker","places","placed","getter","gotten","plated","plates","gently","played","gather","player","please","gating","garden","pocket","gamers","points","pointy","gaming","future","wiping","fuller","police","pooled","poorer","fucked","popped","popper","fronts","friend","freers","poured","pourer","freest","powers","formed","forget","forgot","forest","forces","forced","footed","pretty","follow","fliers","flyers","proven","airing","proves","proved","prover","pulled","flying","puller","flower","pushes","pushed","floors","pusher","flight","fixers","fixing","quicks","winter","fitted","quiets","fitter","winged","radios","rained","raises","raised","fishes","rather","fished","firsts","firing","reader","finish","finger","fining","finest","realer","finder","really","finals","reason","filled","figure","fought","fights","fields","fewest","redder","refuse","remain","feeing","remind","feared","father","faster","remove","repeat","family","faller","fallen","failer","failed","rested","fading","return","reveal","riches","richer","riding","ridden","window","riders","rights","facing","allows","ringed","rising","rivers","extras","rocked","rolled","expect","roofed","excite","except","rooves","roomed","events","rounds","rowing","evened","rubbed","almost","entire","runner","enters","keying","rushed","rushes","sadder","safest","sanded","enjoys","saving","engine","savers","winded","saying","enders","scared","scares","scarer","scenes","ending","school","scream","either","eights","screen","egging","effort","search","edging","seated","second","eaters","seeing","seemed","eating","seller","sender","senses","sensed","easier","easily","earths","serves","served","willed","dusted","settle","during","driers","sevens","sexing","shadow","shakes","shaken","dryers","shaker","always","shaped","driest","shapes","shaper","drying","shares","shared","sharer","sharps","driver","drives","driven","sheets","droves","drinks","shirts","drunks","shoots","dreams","shorts","dozens","should","downed","shouts","shoved","shoves","showed","wilder","shower","dogged","doctor","shrugs","didn't","sicker","sicked","didn't","siding","sighed","doings","sights","signed","dinner","silent","silver","dyings","widest","simple","simply","deeper","single","decide","deaths","sister","deader","sizing","darker","wholes","sleeps","dances","danced","slides","slider","cutter","slower","slowed","slowly","smalls","cupped","smells","smelly","crying","smiles","smiled","smiler","crowds","smokes","smoked","smoker","create","covers","snowed","whited","softer","course","softly","couple","counts","corner","whiter","copped","cooled","cooler","coming","whites","sorted","colors","colder","sounds","coffee","coated","spaces","clouds","spaced","spoken","speaks","clothe","closed","closes","closer","spends","climbs","clears","cleans","spirit","cities","circle","church","choose","spread","chosen","choice","chests","sprung","spring","sprang","stages","stairs","cheeks","stands","keeper","change","chance","stared","stares","starer","chairs","starts","center","causer","caused","states","stated","causes","caught","catted","stayed","steals","stolen","casing","sticks","caring","carded","stones","animal","cannot","stored","stores","storms","answer","camera","calmer","calmed","called","street","buyers","bought","strike","struck","buying","anyone","strong","busier","busied","busing","burner","stuffs","burned","stupid","builds","browns","suites","suited","brings","summer","bright","sunned","bridge","breath","breast","breaks","broken","surest","branch","brains","anyway","boxing","wheels","sweets","swings","bottom","bottle","system","bother","tables","taking","takers","talked","talker","boring","taller","booted","taught","booked","teamed","teared","boning","appear","bodies","thanks","boated","thicks","boards","bluest","things","thinks","blower","thirds","thirty","though","threes","throat","bloods","thrown","throws","blocks","timing","blacks","timers","tinier","biters","tiring","todays","biting","toning","tongue","arming","birded","bigger","wetter","toothy","beyond","better","topped","tossed","bested","tosses","beside","bender","toward","bended","tracks","belong","trains","belief","travel","behind","begins","before","bedded","became","become","beater","beaten","trucks","truest","aren't","aren't","trusts","truths","trying","turned","twenty","around","uncles","weight","wasn't","wasn't","arrive","unless","upping","wedded","viewed","barely","visits","banked","balled","voices","voiced","waited","bagger","waking","walked","bagged","walker","walled","asking","wanted","wanter","warred","waring","backed","warmed","warmer","babies","washed","washes","avoids","attack","waters","asleep","watery","waving","wavers","seems","party","minds","eaten","sells","sends","known","sense","hours","pasts","paths","easts","pause","mined","layer","payed","serve","earth","early","wills","aired","heard","hears","dusts","kills","goers","hotel","seven","dried","ideas","sexed","sexes","going","drier","dries","dryer","glass","heads","shake","leads","shook","aging","gives","phone","local","photo","shape","picks","above","locks","money","drops","share","given","wrong","girls","month","sharp","piece","wilds","sheet","drove","drive","moons","lands","piles","ships","drink","piled","drank","drunk","shirt","pinks","shits","dress","shoes","mores","shoot","longs","shots","dream","drawn","draws","drags","shops","haves","horse","short","gifts","dozen","place","downs","shout","hopes","shove","hoped","plans","wiper","doors","shown","shows","wiped","plate","world","mouth","doers","joins","shrug","shuts","leafs","moved","plays","moves","sicks","don't","pleas","sided","sides","sighs","don't","gated","sight","looks","gates","wives","mover","signs","doing","dirts","knees","movie","learn","gamer","games","gamed","dying","music","since","desks","sings","singe","deeps","point","acted","musts","yells","funny","death","wider","loses","sixes","whose","names","sizes","sized","skins","keyed","skies","pools","slams","darks","named","slept","namer","sleep","leave","dance","slide","hated","young","whole","fucks","who's","slips","who's","slows","front","porch","loved","hates","small","fresh","cries","cried","smell","white","nears","loves","smile","freer","pours","lover","freed","power","smoke","frees","yeses","crowd","cross","jokes","fours","snaps","crazy","forms","cover","homed","snows","among","necks","happy","least","press","force","homes","count","needs","wipes","years","cools","foots","joked","foods","never","songs","comes","sorry","flier","color","sorts","souls","lower","newer","flyer","colds","sound","flown","south","works","coats","space","nicer","prove","lucky","spoke","night","speak","cloud","hurts","yards","pulls","holed","flies","close","climb","spent","spend","words","holes","hangs","clear","lunch","spins","clean","class","liars","floor","holds","spots","alive","noise","flats","chose","flash","nones","child","fixer","fixed","fixes","chest","cheek","mains","stage","hands","makes","stair","quick","stood","check","fiver","stand","stars","fives","north","wrote","stare","lying","quiet","noses","quite","start","chair","nosed","radio","lived","rains","notes","state","large","cause","raise","catch","noted","maker","stays","halls","angry","stole","steal","reach","first","cased","cases","steps","lives","fires","stuck","carry","stick","cares","still","cared","fired","cards","added","stone","reads","halve","stops","write","can't","ready","hairy","store","hairs","can't","storm","numbs","story","could","finer","knife","fines","calms","fined","calls","hurry","while","buyer","finds","nurse","found","which","lifts","admit","final","fills","lasts","keeps","where","buses","bused","study","offed","stuff","fight","woods","burnt","burns","field","human","build","built","wings","offer","brown","allow","guyed","suite","suits","bring","marks","fewer","feels","hills","wines","later","feeds","agree","guess","surer","fears","broke","break","guard","brain","highs","often","marry","ahead","knock","boxes","sweet","boxed","okays","swing","swung","falls","reply","hides","fails","huger","table","takes","taken","laugh","taker","rests","house","talks","bored","women","faded","fades","wheel","facts","wraps","boots","teach","faces","teams","older","books","tears","bones","maybe","woman","faced","areas","boned","opens","tells","rides","grows","thank","their","boats","thens","there","these","thick","rider","after","board","right","bluer","thins","blues","blued","grown","thing","again","rings","think","blows","blown","third","would","means","those","risen","three","rises","blood","eying","heres","throw","block","threw","roses","group","river","black","tying","times","timed","roads","rocks","order","timer","meant","green","tired","tires","extra","meets","today","rolls","biter","bitey","other","toned","tones","light","bites","worry","birds","roofs","armed","outer","rooms","outed","every","tooth","teeth","round","image","bests","event","liked","evens","rowed","likes","touch","bends","windy","bents","towns","winds","great","below","track","overs","owned","liker","train","enter","wound","begun","helps","began","begin","owner","beers","kinds","wests","paged","trees","treed","tripe","trips","pages","alone","hello","beats","enjoy","bears","truck","beach","safer","trues","truer","trued","safes","hells","sames","trust","truth","pains","wells","sands","tried","tries","greys","turns","isn't","isn't","heavy","twice","saves","uncle","saved","under","kicks","saver","paint","lines","grays","until","weeks","upped","pairs","using","asked","usual","scare","being","ender","metal","views","paled","banks","visit","pales","paler","voice","scene","heats","waits","balls","ended","empty","woken","palms","wakes","waked","walks","lined","knows","pants","worse","paper","walls","worst","wants","eight","heart","along","backs","egged","jumps","warms","grass","might","edges","grabs","seats","avoid","parts","edged","aunts","watch","about","eater","won't","water","won't","waved","waves","goods","waver","golds","wears","ears","grab","fits","each","sets","knee","lots","part","dust","noes","fish","stay","good","rain","cats","work","wild","laid","hang","gold","pass","step","loud","case","help","your","past","nods","home","care","path","hell","read","love","fire","gods","lift","card","stop","pays","keys","cars","paid","idea","fine","none","real","into","drop","heat","wish","cans","kids","find","goer","goes","went","calm","just","lead","gone","call","fill","nose","ship","huge","acts","lows","buys","some","note","kind","shit","shat","mind","ices","busy","pick","hand","shod","shoe","gave","reds","shot","hall","fews","ours","feel","burn","drew","such","draw","shop","give","felt","wing","suit","drag","hear","feed","mine","girl","feds","iced","down","when","fees","half","suns","able","word","fear","nows","door","fast","sure","leaf","pile","jobs","show","wine","boys","dogs","yell","hair","guys","kept","doer","fall","fell","head","shut","gift","hole","rest","numb","kick","lean","take","both","sick","fail","fade","took","miss","side","sigh","held","talk","last","plan","bore","hold","done","tall","teas","fact","boot","like","wife","rich","sign","book","wood","team","does","main","offs","tear","tore","torn","rode","dirt","gets","bone","joke","ride","make","told","play","died","tell","dies","tens","area","body","than","boat","line","guns","desk","that","what","kiss","them","they","gate","sang","then","plea","kill","face","sing","sung","eyes","thin","blue","deep","made","rung","ring","sirs","wide","he's","rang","moon","blow","eyed","sits","more","whys","dead","blew","days","this","left","grew","he's","size","rise","rose","whom","have","skin","most","late","grow","slam","road","game","tied","ties","arms","time","dark","rock","okay","ages","mens","roll","mans","tiny","slid","dads","airs","ok'd","tire","wets","ok'd","i'll","roof","slip","full","cuts","pool","slow","tone","bite","lips","cups","bits","room","olds","poor","bird","adds","ever","knew","hate","fuck","pops","even","tops","wipe","hits","once","west","hour","rows","rubs","toss","best","ones","only","from","runs","bend","bent","onto","open","move","town","free","pour","legs","rush","jump","snap","many","hill","less","maps","snow","keep","safe","much","soft","join","beer","i'll","beds","four","tree","same","sand","form","cops","must","year","cool","trip","lets","beat","mark","born","bear","with","come","save","know","true","sons","lock","song","soon","laws","came","outs","name","well","been","says","said","sort","feet","soul","high","yeah","were","hide","foot","turn","cold","wind","yard","twos","coat","food","over","hats","owns","ends","lady","aged","arts","else","long","flew","hurt","page","week","upon","lays","used","uses","hard","eggs","wins","very","mays","seas","pain","near","view","bars","weds","pull","edge","wrap","lies","bank","spin","ball","grey","seat","spun","lied","neck","push","wait","hope","bags","city","look","wake","spot","saws","woke","wear","pink","liar","eats","walk","need","sees","seen","puts","seem","wall","want","pair","gray","sell","will","flat","back","pale","sold","asks","wars","land","send","mean","warm","baby","sent","also","wash","away","here","easy","hung","sens","star","hers","aunt","palm","worn","life","meet","wore","east","live","news","five","wave","next","lost","lose","nice","ways","far","few","war","bad","bag","bar","wed","use","ups","art","was","two","try","are","bed","top","arm","wet","big","too","bit","tie","the","ten","tvs","tea","box","boy","sun","bus","but","buy","any","can","car","cat","and","son","cop","sos","cry","cup","cut","who","dad","sky","day","six","why","sit","sat","sir","die","did","dog","she","dry","sex","set","ear","ate","eat","see","saw","win","won","sea","egg","end","say","sad","ran","run","rub","row","eye","rid","ask","fed","fee","red","way","fit","fix","all","put","fly","for","pop","fun","get","got","god","pay","own","out","our","air","ors","one","old","ohs","gun","key","off","guy","now","not","nor","nod","nos","ago","new","hat","age","had","has","her","met","hey","may","hid","map","him","add","his","man","men","hit","mad","low","lot","hot","lip","how","lit","lie","kid","i'm","let","i'm","leg","i'd","i'd","ice","led","act","lay","law","ins","yes","yet","you","its","job","no","at","by","my","on","ha","do","ok","he","oh","is","tv","me","us","as","hi","go","if","of","am","up","to","we","so","in","or","it","be","an","i","a"]
#Entertainingly, more than 1000 words. Taken from the code at xkcd.com/simplewriter
oscarWinners = ["Birdman","The Grand Budapest Hotel","Whiplash","The Imitation Game","American Sniper","Boyhood","Interstellar","The Theory of Everything","Ida","Selma","Citizenfour","Big Hero 6","Crisis Hotline: Veterans Press 1","The Phone Call","Still Alice","Feast","12 Years a Slave","Gravity","Dallas Buyers Club","Frozen","The Great Gatsby","Her","Blue Jasmine","Mr Hublot","The Lady in Number 6: Music Saved My Life","Helium","The Great Beauty","20 Feet from Stardom","Argo","Life of Pi","Les Miserables","Lincoln","Django Unchained","Skyfall","Silver Linings Playbook","Zero Dark Thirty","Amour","Anna Karenina","Paperman","Brave","Searching for Sugar Man","Inocente","Curfew","The Artist","Hugo","The Iron Lady","The Descendants","The Girl with the Dragon Tattoo","Midnight in Paris","The Help","A Separation","The Fantastic Flying Books of Mr. Morris Lessmore","The Shore","Undefeated","The Muppets","Saving Face","Beginners","Rango","The King's Speech","Inception","The Social Network","The Fighter","Toy Story 3","Alice in Wonderland","Black Swan","In a Better World","The Lost Thing","God of Love","The Wolfman","Strangers No More","Inside Job","The Hurt Locker","Avatar","Precious","Up","Crazy Heart","Inglourious Basterds","Star Trek","The Young Victoria","The Blind Side","Music by Prudence","The Secret in Their Eyes","The Cove","The New Tenants","Logorama","Slumdog Millionaire","The Curious Case of Benjamin Button","Milk","The Dark Knight","WALL-E","The Reader","The Duchess","Departures","Vicky Cristina Barcelona","Smile Pinki","Man on Wire","Toyland","The House of Small Cubes (La Maison en Petits Cubes)","No Country for Old Men","The Bourne Ultimatum","There Will Be Blood","La Vie en Rose","Atonement","Michael Clayton","Ratatouille","Juno","Sweeney Todd: The Demon Barber of Fleet Street","The Golden Compass","Elizabeth: The Golden Age","Taxi to the Dark Side","Peter & the Wolf","Once","The Mozart of Pickpockets (Le Mozart des Pickpockets)","The Counterfeiters (Die Flascher)","Freeheld","The Departed","Pan's Labyrinth (El laberinto del fauno)","Dreamgirls","Little Miss Sunshine","An Inconvenient Truth","Babel","The Queen","Letters from Iwo Jima","Pirates of the Caribbean: Dead Man's Chest","The Danish Poet","Happy Feet","The Last King of Scotland","The Lives of Others (Das Leben der Anderen)","Marie Antoinette","West Bank Story","The Blood of Yingzhou District","Crash","Brokeback Mountain","Memoirs of a Geisha","King Kong","Capote","Walk the Line","The Constant Gardener","The Chronicles of Narnia: The Lion, the Witch and the Wardrobe","Hustle & Flow","Syriana","March of the Penguins (La Marche de l'empereur)","Six Shooter","The Moon and the Son: An Imagined Conversation","A Note of Triumph: The Golden Age of Norman Corwin","Tsotsi","Wallace & Gromit: The Curse of the Were-Rabbit","Million Dollar Baby","The Aviator","Ray","The Incredibles","Finding Neverland","Sideways","Lemony Snicket's A Series of Unfortunate Events","Spider-Man 2","Eternal Sunshine of the Spotless Mind","The Motorcycle Diaries","The Sea Inside","Born into Brothels: Calcutta's Red Light Kids","Mighty Times: The Children's March","Wasp","Ryan","The Lord of the Rings: The Return of the King","Master and Commander: The Far Side of the World","Mystic River","Cold Mountain","Lost in Translation","Finding Nemo","The Barbarian Invasions","Two Soldiers","Monster","Harvie Krumpet","Chernobyl Heart","The Fog of War","Chicago","The Pianist","The Lord of the Rings: The Two Towers","Frida","The Hours","Road to Perdition","Adaptation","Talk to Her (Hable con ella)","This Charming Man (Der Er En Yndig Mand)","Spirited Away","Nowhere in Africa (Nirgendwo in Afrika)","The Chubbchubbs!","Twin Towers","Bowling for Columbine","8 Mile","A Beautiful Mind","The Lord of the Rings: The Fellowship of the Ring","Moulin Rouge!","Black Hawk Down","Gosford Park","Monsters, Inc.","Pearl Harbor","Iris","Shrek","Training Day","Monster's Ball","Thoth","For the Birds","No Man's Land","Murder on a Sunday Morning","The Accountant","Gladiator","Crouching Tiger, Hidden Dragon","Traffic","Erin Brockovich","Almost Famous","Wonder Boys","Dr. Seuss' How the Grinch Stole Christmas (How the Grinch Stole Christmas)","U-571","Pollock","Father and Daughter","Into the Arms of Strangers: Stories of the Kindertransport","Quiero ser (I want to be ...)","Big Mama","American Beauty","The Matrix","The Cider House Rules","Topsy-Turvy","Sleepy Hollow","Boys Don't Cry","Tarzan","One Day in September","The Red Violin (Le violon rouge)","The Old Man and the Sea","My Mother Dreams the Satan's Disciples in New York","King Gimp","Girl, Interrupted","All About My Mother (Todo sobre mi madre)","Shakespeare in Love","Saving Private Ryan","Life Is Beautiful","Elizabeth","Gods and Monsters","The Prince of Egypt","Affliction","What Dreams May Come","The Personals","The Last Days","Election Night (Valgaften)","Bunny","Titanic","Good Will Hunting","L.A. Confidential","As Good as It Gets","The Full Monty","Men in Black","Visas and Virtue","Character (Karakter)","Geri's Game","A Story of Healing","The Long Way Home","The English Patient","Dragonheart","Fargo","Shine","Evita","Jerry Maguire","Independence Day","Emma","Sling Blade","The Ghost and the Darkness","Kolya","The Nutty Professor","Quest","When We Were Kings","Breathing Lessons: The Life and Work of Mark O'Brien","Dear Diary","Braveheart","Apollo 13","Pocahontas","The Usual Suspects","Restoration","Babe","Sense and Sensibility","Il Postino (The Postman)","Dead Man Walking","Leaving Las Vegas","Mighty Aphrodite","Anne Frank Remembered","A Close Shave","Lieberman in Love","One Survivor Remembers","Antonia's Line (Antonia)","Toy Story","Forrest Gump","The Lion King","Speed","Ed Wood","Pulp Fiction","Bullets over Broadway","The Madness of King George","Legends of the Fall","A Time for Justice","Franz Kafka's It's a Wonderful Life","Maya Lin: A Strong Clear Vision","Burnt by the Sun (Utomlyonnye solntsem)","Trevor","The Adventures of Priscilla, Queen of the Desert","Bob's Birthday","Blue Sky","Schindler's List","The Piano","Jurassic Park","Philadelphia","The Fugitive","The Age of Innocence","The Wrong Trousers","Belle Epoque (The Beautiful Era)","I Am a Promise: The Children of Stanton Elementary School","Mrs. Doubtfire","Black Rider (Schwarzfahrer)","Defending Our Lives","Unforgiven","Howards End","Bram Stoker's Dracula","Aladdin","The Crying Game","Scent of a Woman","A River Runs Through It","Indochine","My Cousin Vinny","The Panama Deception","Educating Peter","The Last of the Mohicans","Death Becomes Her","Omnibus","Mona Lisa Descending a Staircase","The Silence of the Lambs","Terminator 2: Judgment Day","Bugsy","JFK","Beauty and the Beast","Thelma & Louise","The Fisher King","In the Shadow of the Stars","Manipulation","Mediterraneo","Session Man","City Slickers","Deadly Deception: General Electric, Nuclear Weapons and Our Environment","Dances with Wolves","Dick Tracy","Ghost","Goodfellas","The Hunt for Red October","Reversal of Fortune","Cyrano de Bergerac","American Dream","Journey of Hope (Reise der Hoffnung)","Days of Waiting","Creature Comforts","The Lunch Date","Misery","Total Recall","Driving Miss Daisy","Glory","Born on the Fourth of July","My Left Foot","The Little Mermaid","Dead Poets Society","The Abyss","Indiana Jones and the Last Crusade","Henry V","The Johnstown Flood","Common Threads: Stories from the Quilt","Cinema Paradiso","Work Experience","Batman","Balance","7 Faces of Dr. Lao","7th Heaven","2001: A Space Odyssey","20,000 Leagues Under the Sea","The Accidental Tourist","The Accused","The Adventures of Don Juan","The Adventures of Robin Hood","The African Queen","Air Force","Airport","The Alamo","The Alaskan Eskimo","Albert Schweitzer","Alexander's Ragtime Band","Alice Doesn't Live Here Anymore","Alien","Aliens","All About Eve","All Quiet on the Western Front","All That Jazz","All That Money Can Buy (The Devil and Daniel Webster)","All the King's Men","All the President's Men","Ama Girls","Amadeus","Amarcord","America, America","An American in Paris","An American Werewolf in London","Amphibious Fighters","Anastasia","Anchors Aweigh","The Anderson Platoon (La Section Anderson)","Angel and Big Joe","Anna & Bella","Anna and the King of Siam","Anne of the Thousand Days","Annie Get Your Gun","Annie Hall","Anthony Adverse","The Apartment","Apocalypse Now","The Appointments of Dennis Jennings","Aquatic House Party","Arise, My Love","Around the World in Eighty Days","Arthur","Arthur Rubinstein - The Love of Life (L'amour de la vie - Artur Rubinstein)","Artie Shaw: Time Is All You've Got","The Assault (De Aanslag)","The Awful Truth","Babette's Feast (Babettes gaestebud)","The Bachelor and the Bobby-Soxer","Back to the Future","The Bad and the Beautiful","Bad Girl","The Barefoot Contessa","Barry Lyndon","The Battle of Midway","Battleground","Bear Country","Becket","Bedknobs and Broomsticks","Beetlejuice","Being There","The Bells of St. Mary's","Ben-Hur","Benjy","The Bespoke Overcoat","Best Boy","The Best Years of Our Lives","Beyond the Line of Duty","The Bicycle Thief","The Big Broadcast of 1938","The Big Country","The Big House","Bill and Coo","Bird","Birds Anonymous","The Bishop's Wife","Black and White in Color (Noirs et blancs en couleur)","Black Fox: The Rise and Fall of Adolf Hitler (The Black Fox)","Black Narcissus","Black Orpheus (Orfeu Negro)","The Black Stallion","The Black Swan","Blithe Spirit","Blood and Sand","Blood on the Sun","Blossoms in the Dust","Board and Care","Body and Soul","The Bolero","Bonnie and Clyde","Bored of Education","Born Free","Born Yesterday","Bound for Glory","The Box","A Boy and His Dog","Boys and Girls","Boys Town","The Brave One","Breakfast at Tiffany's","Breaking Away","Breaking the Sound Barrier","The Bridge of San Luis Rey","The Bridge on the River Kwai","The Bridges at Toko-Ri","Broadway Melody of 1936","The Broadway Melody","Broken Lance","Broken Rainbow","The Buddy Holly Story","Bullitt","Busy Little Bears","Butch Cassidy and the Sundance Kid","BUtterfield 8","Butterflies Are Free","Cabaret","Cactus Flower","Calamity Jane","California Suite","Call Me Madam","Camelot","The Candidate","Captain Carey, U.S.A.","Captains Courageous","Casablanca","Casals Conducts: 1964","Cat Ballou","The Cat Concerto","Cavalcade","Chagall","The Champ","Champion","A Chance to Live","Charade","The Charge of the Light Brigade","Chariots of Fire","Charly","The Chicken (Le Poulet)","Children of a Lesser God","Chinatown","A Christmas Carol","Churchill's Island","Cimarron","The Circus","Citizen Kane","City of Wax","Cleopatra","Cleopatra","Climbing the Matterhorn","Close Encounters of the Third Kind","Close Harmony","Closed Mondays","Closely Watched Trains (Ostre sledovane vlaky)","Coal Miner's Daughter","Cocoon","The Color of Money","Come and Get It","Come Back, Little Sheba","Coming Home","Cool Hand Luke","Coquette","The Country Cousin","The Country Girl","Cover Girl","The Cowboy and the Lady","Crac","Crash Dive","Crashing the Water Barrier","Cries and Whispers (Viskningar och rop)","The Critic","Cromwell","The Crunch Bird","La Cucaracha","Cyrano de Bergerac","Czechoslovakia 1968","A Damsel in Distress","Dangerous","Dangerous Liaisons","Dangerous Moves (La Diagonale du fou)","The Dark Angel","Darling","The Dawn Patrol","Day for Night (La Nuit americaine)","Day of the Painter","Daybreak in Udi","Days of Heaven","Days of Wine and Roses","Death on the Nile","December 7th","Declaration of Independence","The Deer Hunter","The Defiant Ones","Der Fuehrer's Face","Dersu Uzala","Desert Victory","Design for Death","Designing Woman","Destination Moon","The Diary of Anne Frank","Dirty Dancing","The Dirty Dozen","The Discreet Charm of the Bourgeoisie (Le charme discret de la bourgeoisie)","Disraeli","The Divine Lady","Divorce Italian Style","The Divorcee","Doctor Dolittle","Doctor Zhivago","Dodsworth","Dog Day Afternoon","The Dollar Bottom","Don't","The Dot and the Line (The Dot and the Line: A Romance in Lower Mathematics)","A Double Life","The Dove","Down and Out in America","Dr. Jekyll and Mr. Hyde","Dumbo","Dylan Thomas","E.T.: The Extra-Terrestrial","Earthquake","East of Eden","Easter Parade","The Eleanor Roosevelt Story","Elmer Gantry","The Empire Strikes Back","The End of the Game","The Enemy Below","Eskimo","Every Child","Exodus","The Exorcist","The Face of Lincoln","Facing Your Danger","The Facts of Life","Fame","Fanny & Alexander (Fanny och Alexander)","Fantasia","Fantastic Voyage","A Farewell to Arms","The Farmer's Daughter","Father Goose","Federico Fellini's Eight and a half","Fellini's Casanova (Il Casanova di Federico Fellini)","Ferdinand the Bull","Fiddler on the Roof","The Fighting Lady","First Steps","A Fish Called Wanda","Flamenco at 5:15","Flashdance","The Flight of the Gossamer Condor","Flowers and Trees","The Fly (A Legy)","The Fly","Folies Bergere","For Scent-imental Reasons","For Whom the Bell Tolls","Forbidden Games","A Force in Readiness","The Fortune Cookie","Frank Film","A Free Soul","The French Connection","Frenchman's Creek","From Here to Eternity","From Mao to Mozart: Isaac Stern in China","Funny Girl","A Funny Thing Happened on the Way to the Forum","Gandhi","The Garden of Allah","The Garden of the Finzi-Continis (Il Giardino dei Finzi-Contini)","Gaslight","Gate of Hell (Jigokumon)","The Gay Divorcee","Genocide","Gentleman's Agreement","Gerald McBoing-Boing","Get Out Your Handkerchiefs (Preparez vos mouchoirs)","Giant","Gigi","Giuseppina","Give Me Liberty","Glass (Glas)","The Glenn Miller Story","The Godfather","The Godfather Part II","Going My Way","Gold Diggers of 1935","The Golden Fish (Histoire d'un poisson rouge)","Goldfinger","Gone with the Wind","The Good Earth","The Goodbye Girl","Goodbye, Miss Turlock","Goodbye, Mr. Chips","The Graduate","Grand Canyon","Grand Hotel","Grand Prix","Grandad of Races","The Grapes of Wrath","Gravity Is My Enemy","Great (Great (Isambard Kingdom Brunel))","The Great American Cowboy","The Great Caruso","Great Expectations","The Great Gatsby","The Great Lie","The Great McGinty","The Great Race","The Great Waltz","The Great Ziegfeld","The Greatest Show on Earth","A Greek Tragedy","Green Dolphin Street","Guess Who's Coming to Dinner","The Guns of Navarone","Hamlet","Hannah and Her Sisters","Happy Anniversary (Heureux Anniversaire)","Harlan County, USA","Harry and the Hendersons","Harry and Tonto","Harvey","The Harvey Girls","He Makes Me Feel Like Dancin'","Hearts and Minds","Heaven Can Wait","Heavenly Music","The Heiress","Helen Keller in Her Story (The Unconquered)","Hello, Dolly!","Hello, Frisco, Hello","The Hellstrom Chronicle","Henry V","A Herb Alpert and the Tijuana Brass Double Feature","Here Comes Mr. Jordan","Here Comes the Groom","The High and the Mighty","High Noon","The Hindenburg","Hitler Lives","A Hole in the Head","The Hole","Holiday Inn","The Horse with the Flying Tail","The Hospital","Hotel Terminus: The Life and Times of Klaus Barbie","The House I Live In","The House on 92nd Street","How Green Was My Valley","How the West Was Won","How to Sleep","Hud","The Human Comedy","The Hurricane","The Hustler","I Want to Live!","I Wanted Wings","I Won't Play","If You Love This Planet","I'll Cry Tomorrow","I'll Find a Way","In Beaver Valley","In Old Arizona","In Old Chicago","In the Heat of the Night","In the Region of Ice","In Which We Serve","Indiana Jones and the Temple of Doom","The Informer","Innerspace","Interrupted Melody","Interviews with My Lai Veterans","The Invaders","Investigation of a Citizen Above Suspicion (Indagine su un cittadino al di sopra di ogni sospetto)","Irma la Douce","Is It Always Right to Be Right?","It Happened One Night","It's a Mad, Mad, Mad, Mad World","It's Tough to Be a Bird","Jaws","The Jazz Singer","Jezebel","Joan of Arc","Johann Mouse","Johnny Belinda","Johnny Eager","The Joker Is Wild","The Jolson Story","Journey into Self","Judgment at Nuremberg","Julia","Julius Caesar","Just Another Missing Kid","Karl Hess: Toward Liberty","Kentucky","Key Largo","The Killing Fields","The King and I","King Kong","King of Jazz","King Solomon's Mines","Kiss of the Spider Woman","Kitty Foyle (Kitty Foyle: The Natural History of a Woman)","Klute","Knighty Knight Bugs","Kokoda Front Line","Kon-Tiki","Krakatoa","Kramer vs. Kramer","Kukan","La Strada (The Road)","La Dolce Vita","Lady Be Good","The Last Command","The Last Emperor","The Last Picture Show","Laura","The Lavender Hill Mob","Lawrence of Arabia","Leave Her to Heaven","Leisure","Lend a Paw","Les Girls","Let It Be","A Letter to Three Wives","The Life of Emile Zola","Light in the Window","Lili","Lilies of the Field","Limelight","The Lion in Winter","The Little Kidnappers","A Little Night Music","The Little Orphan","A Little Romance","Little Women","Little Women","The Lives of a Bengal Lancer","The Living Desert","Logan's Run","The Longest Day","Lost Horizon","The Lost Weekend","Love Is a Many-Splendored Thing","Love Me or Leave Me","Love Story","Lovers and Other Strangers","Lust for Life","Madame Rosa (La Vie devant soi)","The Magic Machines","Magoo's Puddle Jumper","Main Street on the March!","A Man and a Woman","A Man for All Seasons","The Man Who Knew Too Much","The Man Who Planted Trees (L' Homme qui plantait des arbres)","The Man Who Skied Down Everest","Manhattan Melodrama","Marie-Louise","Marjoe","Marooned","Marty","Mary Poppins","M*A*S*H","Mask","Melvin and Howard","Men Against the Arctic","Mephisto","The Merry Widow","Midnight Cowboy","Midnight Express","A Midsummer Night's Dream","Mighty Joe Young","The Milagro Beanfield War","Mildred Pierce","The Milky Way","Min and Bill","Miracle on 34th Street","The Miracle Worker","Missing","The Mission","Mississippi Burning","Mister Roberts","Molly's Pilgrim","Monsieur Vincent","Moonbird","Moonstruck","The More the Merrier","Morning Glory","Moscow Does Not Believe in Tears","Moscow Strikes Back","Mother Wore Tights","Moulin Rouge","Mouse Trouble","Mr. Deeds Goes to Town","Mr. Smith Goes to Washington","Mrs. Miniver","Munro","Murder on the Orient Express","The Music Box","The Music Man","Mutiny on the Bounty","My Fair Lady","My Gal Sal","My Uncle (Mon oncle)","The Naked City","Nashville","National Velvet","Nature's Half Acre","Naughty Marietta","Neighbours","Neptune's Daughter","Network","Never on Sunday (Pote tin Kyriaki)","Nicholas and Alexandra","The Night of the Iguana","Nights of Cabiria (Le Notti di Cabiria)","Nine from Little Rock","None But the Lonely Heart","Norma Rae","Norman Rockwell's World... An American Dream","North West Mounted Police","Now, Voyager","Number Our Days","An Occurrence at Owl Creek Bridge","Of Pups and Puzzles","An Officer and a Gentleman","The Official Story (La Historia Oficial)","Oklahoma!","The Old Man and the Sea","The Old Mill","Oliver!","The Omen","On Golden Pond","On the Town","On the Waterfront","One Flew over the Cuckoo's Nest","One Hundred Men and a Girl","One Night of Love","One Way Passage","One-Eyed Men Are Kings (...borgnes sont rois, Les)","Ordinary People","Out of Africa","Overture to The Merry Wives of Windsor","The Paleface","Panic in the Streets","Papa's Delicate Condition","The Paper Chase","Paper Moon","A Passage to India","A Patch of Blue","The Patriot","Patton","Paul Robeson: Tribute to an Artist","Pelle the Conqueror (Pelle erobreren)","Penny Wisdom","Phantom of the Opera","The Philadelphia Story","Picnic","The Picture of Dorian Gray","Pillow Talk","The Pink Phink","Pinocchio","A Place in the Sun","A Place to Stand (A Place to Stand, A Place to Grow)","Places in the Heart","Planet of the Apes","Platoon","Plymouth Adventure","Pollyanna","Porgy and Bess","Portrait of Jennie","The Poseidon Adventure","Precious Images","Prelude To War","Pride and Prejudice","The Pride of the Yankees","The Prime of Miss Jean Brodie","Princess O'Rourke","Princeton: A Search for Answers","The Private Life of Henry VIII","The Private Life of the Gannets","Prizzi's Honor","The Producers","Project Hope","The Public Pays","Purple Rain","Pygmalion","Quest for Fire","Quicker'n a Wink","The Quiet Man","Quiet Please!","Raging Bull","Raiders of the Lost Ark","Rain Man","The Rains Came","Ran","Rashomon","Ray's Male Heterosexual Dance Hall","The Razor's Edge","Reap the Wild Wind","Rebecca","The Red Balloon (Le ballon rouge)","The Red Shoes","Reds","The Redwoods","The Resurrection of Broncho Billy","Return of the Jedi","The Right Stuff","The River","The Robe","Robert Frost: A Lover's Quarrel with the World","Robert Kennedy Remembered","RoboCop","Rocky","Roman Holiday","Romeo and Juliet","Room at the Top","A Room with a View","The Rose Tattoo","Rosemary's Baby","Round Midnight","Ryan's Daughter","Sabrina","Samson and Delilah","Samurai I: Musashi Miyamoto (Miyamoto Musashi)","San Francisco","The Sand Castle (Le Chateau de sable)","The Sandpiper","Save the Tiger","Sayonara","Scared Straight!","The Scoundrel","The Sea Around Us","Seal Island","The Search","Seawards the Great Ships","The Secret Land","Seeds of Destiny","Sentinels of Silence","Separate Tables","Serengeti Shall Not Die (Serengeti darf nicht sterben)","Sergeant York","Seven Brides for Seven Brothers","Seven Days to Noon","The Seventh Veil","Shaft","Shampoo","Shane","Shanghai Express","She Wore a Yellow Ribbon","Ship of Fools","A Shocking Accident","Shoeshine (Sciuscia)","The Shop on Main Street (Obchod na korze)","The Silent World (Le Monde du silence)","The Sin of Madelon Claudet","Since You Went Away","Skippy","Sky Above and Mud Beneath (Le Ciel et la boue)","The Snake Pit","Snow White and the Seven Dwarfs","So Much for So Little","So This Is Harris!","The Solid Gold Cadillac","Some Like It Hot","Somebody Up There Likes Me","The Song of Bernadette","Song of the South","Song Without End","Sons and Lovers","Sons of Liberty","Sophie's Choice","The Sound of Music","South Pacific","Spartacus","Spawn of the North","Speaking of Animals and Their Families","Special Delivery","Speedy Gonzales","Spellbound","Splendor in the Grass","Stagecoach","Stairway to Light","Stalag 17","Star in the Night","A Star Is Born","A Star Is Born","Star Wars","State Fair","The Sting","The Stone Carvers","The Story of Louis Pasteur","The Stratton Story","Street Angel","A Streetcar Named Desire","Strike Up the Band","The Subject Was Roses","The Substitute (Surogat)","Summer of '42","Sundae in New York","Sundays and Cybele (Le Dimanches de Ville d'Avray)","Sunrise","Sunset Boulevard","The Sunshine Boys","Superman","Survival City","Suspicion","Sweet Bird of Youth","Sweethearts","Swing Time","Symphony of a City","Tabu","Tango","Target for Tonight","Teddy, the Rough Rider","Teenage Father","Tempest","The Ten Commandments","Tender Mercies","The Ten-Year Lunch: The Wit and Legend of the Algonquin Round Table","Terms of Endearment","Tess","Thank God It's Friday","That Hamilton Woman","That Mothers Might Live","They Shoot Horses, Don't They?","The Thief of Bagdad","The Third Man","Thirty Seconds Over Tokyo","This Above All","This Is the Army","This Land Is Mine","This Mechanical Age","This Tiny World","The Thomas Crown Affair","Thoroughly Modern Millie","A Thousand Clowns","Three Coins in the Fountain","The Three Faces of Eve","Three Little Pigs","Three Orphan Kittens","Through a Glass Darkly (Sasom i en spegel)","Thunderball","Thursday's Children","The Time Machine","A Time Out of War","The Times of Harvey Milk","The Tin Drum (Die Blechtrommel)","Tin Pan Alley","Tin Toy","The Titan: Story of Michelangelo","Titanic","To Be Alive!","To Begin Again (Volver a empezar)","To Catch a Thief","To Each His Own","To Kill a Mockingbird","Tom Jones","tom thumb","Toot, Whistle, Plunk and Boom","Tootsie","Top Gun","Topkapi","Tora! Tora! Tora!","The Tortoise and the Hare","Torture Money","A Touch of Class","Toward Independence","The Towering Inferno","Transatlantic","Travels with My Aunt","The Treasure of the Sierra Madre","A Tree Grows in Brooklyn","The Trip to Bountiful","The True Glory","True Grit","The True Story of the Civil War","Tweetie Pie","Twelve O'Clock High","Two Arabian Knights","The Two Mouseketeers","Two Women (La Ciociara)","The Ugly Duckling","Underworld","The Untouchables","Up","The V.I.P.s","Vacation from Marriage (UK title Perfect Strangers)","Van Gogh","The Vanishing Prairie","Victor Victoria","Violet","The Virgin Spring (Jungfrukallan)","Viva Villa!","Viva Zapata!","Waikiki Wedding","Wall Street","The Walls of Malapaga","War and Peace (Voyna i mir)","The War Game","The War of the Worlds","Watch on the Rhine","Water Birds","The Way of All Flesh","The Way We Were","West Side Story","The Westerner","The Wetback Hound","What Ever Happened to Baby Jane?","When Tomorrow Comes","When Magoo Flew","When Worlds Collide","White Nights","White Shadows in the South Seas","White Wilderness","Who Are the DeBolts? And Where Did They Get Nineteen Kids?","Who Framed Roger Rabbit","Who's Afraid of Virginia Woolf?","Who's Who in Animal Land","Why Korea?","Why Man Creates","Wild Wings","Wilson","Wings","Wings Over Everest","Winnie the Pooh and the Blustery Day","With a Song in My Heart","With Byrd at the South Pole","With the Marines at Tarawa","Witness","Witness to War: Dr. Charlie Clements","The Wizard of Oz","The Woman in Red","Woman of the Year","Women - for America, for the World","Women in Love","Wonder Man","The Wonderful World of the Brothers Grimm","Woodstock","Working Girl","World of Kids","World Without Sun (Le Monde sans soleil)","Wrestling Swordfish","Written on the Wind","Wuthering Heights","Yankee Doodle Dandy","The Yankee Doodle Mouse","The Year of Living Dangerously","A Year Toward Tomorrow","The Yearling","Yentl","Yesterday, Today and Tomorrow (Ieri, oggi, domani)","You Can't Take It with You","You Don't Have to Die","You Light Up My Life","Young at Heart","Z","Zorba the Greek (Alexis Zorbas)"]

def getInvalidWords(story):
	invalidWords = [];
	for word in story.split():
		if word not in validWords:
			invalidWords.append(word)
	return invalidWords

# Ten points per personally-described character whose fate we know by the end of the story
def characters(story):
	return 0


#ln(87) points per different Oscar-winning movie title included, up to a limit of five. (You can change punctuation, capitalisation and spell numbers out)
def oscar(story):
	#I reckon the easiest are 'her', 'wings', 'up',  'the fly',  'don't', 'the box', 'bird', 'for the birds', 'once'
	#"Back to the future" is also notable...
	score = 0
	for winner in oscarWinners:
		if winner.translate(string.maketrans("",""), string.punctuation).lower() in story:
			score+=math.log(87)
	return min(score, math.log(87) * 5)



#10 *SQRT(n) points for the longest run of n consecutive lines of iambic pentameter (you don't have to put line breaks in)
def pentameter(story):
	d = cmudict.dict()
	storywords = story.split()
	storyStresses = ""
	for word in storywords:
		pronuns = d[word.lower()]
		options = []
		for pronun in pronuns: #Some words can be pronounced multiple ways...
			stresses = ""
			for syllable in pronun:
				if syllable[-1].isdigit():
					stresses+=syllable[-1]
			options.append(stresses)
			if stresses=="1":
				options.append("0") #Seems to have single-syllables as 1, but they can be 0 too

		addedWordStress = False
		if storyStresses=="" or storyStresses[-1]=='1':
			#We want to start with a 0 stress if possible
			for option in options:
				if option[0]=='0' and addedWordStress==False:
					storyStresses+=option
					addedWordStress = True
		else:
			#We want to start with a 1 stress if possible
			for option in options:
				if option[0]=='1' and addedWordStress==False:
					storyStresses+=option
					addedWordStress = True

		if addedWordStress==False:#If there was no such pronunciation, add one anyway. Maybe this can be the start of great things...
			storyStresses += options[0]

	#Story stresses now contains all the stresses in the story. How many times do we have 0101010101, which represents
	#a line of iambic pentameter?
	nlines = 1
	while '01'*5*nlines in storyStresses:
		nlines+=1
	return 10 * math.sqrt(nlines-1)

#Sqrt(n) points where n is the sum of the squares of the lengths of your sentences which are acrostics of valid words
def acrostic(story):
	n= 0;
	sentences = re.split(r' *[\.\?!][\'"\)\]]* *', story) #No-one get cocky with their punctuation, okay?
	for sentence in sentences:
		acrosticWord = "".join([i[0] for i in sentence.split()]) #I f***ing love python sometimes
		if acrosticWord.lower() in validWords:
			n+=len(sentence.split())**2

	return math.sqrt(n)

#pi * sqrt(n) points for the longest run of n words in a row whose lengthhs (mod 10 make up the first n digits of pi)
def pi(story):
    pi = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091"
    piindex = 0
    storyindex = 0
    currentrun=[]
    maxrun = []
    storywords= story.split()
    for word in storywords:
        if len(word)%10==int(pi[piindex]):
            currentrun.append(word)
            piindex+=1
            if len(currentrun) > len(maxrun):
            	maxrun = currentrun
        else:
            currentrun=[]
            piindex=0

    return float(pi)*1e-250 * math.sqrt(len(maxrun))

#ln(118) * SQRT(n) points for the longest run of n words in a row that can be made of chemical element symbols (ingoring spaces and punctuation and capitalisation)
def elements(story):
	symbols= ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Uut","Fl","Uup","Lv","Uus","Uuo"]
	symbols = [x.lower() for x in symbols]

	global maxwords
	maxwords = 0

	def possibleNextElements(inputString, elementsSeen, words):
		global maxwords
		if inputString=="":
			#end of string counts as end of word if we've finished cleanly
			if words+1 > maxwords:
				maxwords = words+1

		else:
			#We want to skip the space in the next 1/2/3 letters if there is one
			hasSpace=0


			if inputString[0]==" ":
				if words+1 > maxwords:
					maxwords = words+1
				possibleNextElements(inputString[1:], elementsSeen, words+1)
				#Then we've finished cleanly on a word. This counts!

			elif inputString[0:1] in symbols:
				elementsSeen.append(inputString[0:1])
				possibleNextElements(inputString[1:],elementsSeen, words )
				del elementsSeen[-1]


			if len(inputString)>2 and inputString[1]==" ":
				hasSpace=1
			if len(inputString)>=2+hasSpace and inputString[0:2+hasSpace].replace(" ", "") in symbols:
				elementsSeen.append(inputString[0:2+hasSpace].replace(" ", ""))
				possibleNextElements(inputString[2+hasSpace:],elementsSeen, words + hasSpace )
				del elementsSeen[-1]

			if len(inputString)>3 and inputString[2]==" ":
				hasSpace=1
			if len(inputString)>=3+hasSpace and inputString[0:3+hasSpace].replace(" ", "") in symbols:
				elementsSeen.append(inputString[0:3+hasSpace].replace(" ", ""))
				possibleNextElements(inputString[3+hasSpace:].replace(" ", ""),elementsSeen, words + hasSpace )
				del elementsSeen[-1]

	storywords = story.split()
	for idx in range(len(storywords)):
		possibleNextElements(" ".join(storywords[idx:]), [], 0)
	return math.log(118) * math.sqrt(maxwords)


#3 *sqrt(n) points for the longest run of n words in a row that are in alphabetical order
def alphabetical(story):
	storyindex = 0
	currentrun=0
	maxrun=0
	prevWord=""
	words = []
	storywords = story.split()
	for word in storywords:
		if word>prevWord:
			currentrun+=1
			words.append(word)
			if currentrun>maxrun:
				maxrun=currentrun
				maxwords = words
		else:
			currentrun=1
			words = [word]
		prevWord=word

	return 3 * math.sqrt(maxrun), maxwords

#1.52 * sqrt(n) points if a string of consecutive words in your story anagrams to the names of two stations on the same London Underground line, the shortest route between which on that line has n stops. Scored up to a limit of three times on different lines.
import networkx as nx
import math
import csv
import string
import operator
G=nx.Graph()

def standardise(instr):
    return ''.join(sorted(''.join(instr.split()).lower()))

# Import london underground data, taken from
# https://commons.wikimedia.org/wiki/London_Underground_geographic_maps/CSV
with open('./data/stations.dat', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader, None)  # skip the headers
    for row in spamreader:
    	stationname = row[3].replace('5','Five')
        G.add_node(row[0], name=row[3])

stations = nx.get_node_attributes(G, "name")


lines={}
with open('./data/routes.dat', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader, None)  # skip the headers
    for row in spamreader:
        lines[row[0]] = row[1]


undergroundScores = {}
for line in lines:
    #Remove all connections
    G = nx.create_empty_copy(G)
    stations_on_this_line = []
    with open('./data/lines.dat', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            if row[2]==line:
                G.add_edge(row[0], row[1])
                if (row[0] not in stations_on_this_line):
                    stations_on_this_line.append(row[0])
                if (row[1] not in stations_on_this_line):
                    stations_on_this_line.append(row[1])


    for idx, station in enumerate(stations_on_this_line):
        for idy, station2 in enumerate(stations_on_this_line):
            if idy>idx:
                path_length = nx.shortest_path_length(G, station, station2)
                undergroundScores[standardise((stations[station] + stations[station2]).translate(string.maketrans("",""), string.punctuation).lower())] = {"station1": stations[station], "station2": stations[station2],"line":lines[line], "score": 1.52 * math.sqrt(path_length)}

def underground(story):
	storywords = story.split()
	longest_key = max(len(x) for x in undergroundScores)
	idx = 0
	idy = 1
	storyScores = {}
	while idx < len(storywords) :
		testwords = "".join(storywords[idx:idy])
		if standardise(testwords) in undergroundScores:
			#It scores us points!
			if (undergroundScores[standardise(testwords)]['line'] in storyScores):
				if undergroundScores[standardise(testwords)]['score'] > storyScores[undergroundScores[standardise(testwords)]['line']]:
					storyScores[undergroundScores[standardise(testwords)]['line']] = undergroundScores[standardise(testwords)]['score']
			else:
				storyScores[undergroundScores[standardise(testwords)]['line']] = undergroundScores[standardise(testwords)]['score']
		if len(testwords)>longest_key:
			idx+=1
			idy=idx+1
		else:
			idy+=1
		if idy > len(storywords):
			idx+=1
			idy=idx+1

	#take top 3 lines that scored us points
	sorted_x = sorted(storyScores.items(), key=operator.itemgetter(1), reverse=True)
	score = 0
	for idx, val in enumerate(sorted_x):
		if idx < 3:
			score += val[1]

	return score


#n points where n! is the greatest factorial dividing the product of the lengths of all sentences in the story.
def factorial(story):
	sentences = re.split(r' *[\.\?!][\'"\)\]]* *', story) #No-one get cocky with their punctuation, okay?
	product=1
	for sentence in sentences:
		if sentence.strip() != '':
			product = product * len(sentence.strip().split())
	#Now find the greatest factorial
	n = 1
	while product % math.factorial(n) ==0:
		n+=1

	return n-1

#n words for the greatest n such that you use exactly n different n-letter words
def nDifferentNLetter(story):
	words = story.split();
	histogram = {}
	for word in words:
		wordlength = len(word)
		if (wordlength not in histogram):
			histogram[wordlength]=[word]
		elif word not in histogram[wordlength]:
			histogram[wordlength].append(word)

	score = 0
	for length in histogram:
		if len(histogram[length])==length and length > score:
			score = length
	return score

#15 exp(-ln(n/9)^2) points if you don't use any words that score n in scrabble, for the n which makes this biggest
def scrabble(story):

	def scrabble_score(word):
		points = {"a":1, "b":3, "c":3, "d":2, "e":1,"f":4, "g":2, "h":4, "i":1, "j":8, "k":5, "l":4, "m":3, "n":1, "o":1, "p":2, "q":10, "r":1, "s":1, "t":1, "u":1, "v":4, "w":4, "x":8, "y":4, "z":10}
		total=0
		for char in word:
			total = total + points[char]
		return total

	scores = {}
	words = story.split();
	for word in words:
		score = scrabble_score(word)
		scores[score] = True

	idx = 1
	score = 0
	while idx <100:
		if (idx not in scores):
			#Then this might be worth points
			potscore = 15*math.exp(-(math.log(idx/9.0))**2)
			if potscore > score:
				score = potscore
		idx+=1

	#Plotting this shows that the peak is 9? Seems about right...
	return score

#(n-13)^2/13 points if you use exactly n of the letters of the alphabet an odd number of times
def alphabet(story):
	histogram = {}
	for letter in story:
		if letter in histogram:
			histogram[letter]+=1;
		else:
			histogram[letter]=1
	nOddLetters = 0
	for letter in histogram:
		if histogram[letter]%2==1:
			nOddLetters+=1
	return (nOddLetters-13)**2 / 13.0


if __name__ == '__main__':
	import sys
	with open(sys.argv[1], 'r') as f:
		story = f.read()

	storynopunct = story.translate(string.maketrans("",""), string.punctuation).lower() #Remove punctuation, lowercase story

	if (len(storynopunct.split())>250):
		print "Story is too long at ", len(storynopunct.split()), 'words'
	if len(getInvalidWords(storynopunct))==0:
		print "="*80
		print "Oscar score:", oscar(storynopunct)
		print "Iambic pentameter:", pentameter(storynopunct)
		print "Acrostic:", acrostic(story)
		print "Pi:", pi(storynopunct)
		print "Elements:", elements(storynopunct)
		print "Alphabetical order:", alphabetical(storynopunct)
		print "Underground: ", underground(storynopunct)
		print "Factorial:", factorial(story)
		print "Different letters:", nDifferentNLetter(storynopunct)
		print "Scrabble:" , scrabble(storynopunct)
		print "Alphabet:", alphabet(storynopunct)
		print "-"*80
		print 'Total score: ',  characters(story) + oscar(storynopunct) + pentameter(storynopunct) + acrostic(story) + pi(storynopunct) + elements(storynopunct) + alphabetical(storynopunct)[0] + underground(storynopunct) + factorial(story) + nDifferentNLetter(storynopunct) + scrabble(storynopunct) + alphabet(storynopunct)
		print "="*80
	else:
		print 'Your story contains invalid words:', getInvalidWords(story)