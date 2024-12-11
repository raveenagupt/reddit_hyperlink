import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

top_25_subreddits = ["rightist", "universityofsussex", "applemusic", "pentesting", "justicedemocrats", "italygames", "hardcoresmp", "floridaman", "idaho", "silphroadaustralasia", "super_nerd92", "talesfromtamriel", "cretoriani", "unsubscribed", "aoe3", "conservativesonly", "superleague", "acura", "the_schulz_meta", "hydro", "msabroad", "westsussex", "silphroadasia", "angular2", "businessintelligence", "minesmash", "1fcnuernberg", "sunglasses", "gunnnife", "fx0", "doraiso", "redditemblemfates", "olympiakosfc", "strike4democracy", "clubpenguin", "multiplayerdotonion", "charlottesville", "gtavadventures", "ecigclassifiedsuk", "sysadminresumes", "operationmoonshot", "killyourconsole", "gameofmoney", "ineedtotalktosomeone", "project_aquarius", "finalproject", "southwales", "mgo", "tatterjack", "frenchhouse", "calexil", "sflist", "reddittango", "renssiesdev", "igotmygjallarhorn", "writewithme", "pygame", "listsandlinks", "fnafblender", "nujabes", "tryptonaut", "underreportednews", "pitt", "netflixcanada", "nsfw_html5", "listentocirclejerk", "teaparty", "ratchetandclank", "modelaushr", "shitanarchistssay", "vltgark", "cloudtobutt", "herdofsquirrels", "division", "ula", "dceuleaks", "kitchens", "chicagobears", "setuptest", "illinoisamiibo", "neoscavenger", "davidlynch", "rugbyleague", "nexusplayer", "helpmebuildapc", "depression_help", "modelnewstatesman", "vodsprivate", "leftistconversation", "ransomware", "portugaltheman", "deathsquad", "strikeaction", "blacksteelalliance", "slurpyderpy", "scrubs", "liswrites", "goldbenefits", "computerwargames", "user_simulator", "rollme", "ikemains", "gtavmoneyhax", "savidenec", "cannacoin", "sssserver", "austinclassifieds", "dreamcast", "donaldtrump2016", "sciencefacts", "arm", "larp", "bayareaamiibros", "cooljak96", "stairsinthewoods", "skydiving", "depressed", "openandhonest", "mobilelegends", "jltieba", "ebikes", "internationalbaseball", "dcevents", "makesyoumoist", "dnd5th", "atc", "redvsblue", "shittybattlestations", "cheekyasian", "xboxbadabing", "h2kgaming", "msilaptops", "unccharlotte", "boolberry", "snsd", "gtamoneydrop", "apologetics", "duckdose", "asktech", "michiganwolverines", "tuftrt", "dungeonprompt", "dangak", "soylentmarket", "subredditcontests", "noahsotherark", "modelinnocenceproject", "teflshit", "freecosmos", "overwatchcustomgames", "aphextwin", "unionhouse", "terps", "clannad", "pastafarianism", "houseofcards", "gakkougurashi", "leagueoflinux", "teachinginjapan", "springbranch", "blacksmithpcw", "eupersonalfinance", "rickygervais", "zorbex", "odenknight_sto", "bergecraft", "stevenuniversefanfic", "femininenotfeminist", "weeklyplanetpodcast", "onemoreguy", "howyoudoin", "mirrorsedge", "rollerderby", "quotesincontext", "teamastersmafia", "oraistedearg", "darkpitmains", "scienceteachers", "mbta", "turk_raffle", "lesbiangamers", "gayporn", "ogn", "qzrestaurant", "bbredditinfinity", "cosmicdisclosure", "anglish", "mallninjashit", "decaf", "jurri", "survivalunion", "flat_earth", "fantasymls", "itunes", "redditepsilon", "logic_301", "motheroflearning", "spacediscussions", "holland", "substrata", "modelusmeta", "greenhouses", "communist", "theredwoman", "fightsticks", "thunderbirds", "newhaven", "sgap", "usps", "alternative_right", "starcitizenfrance", "vagrant", "googlemusic", "splatoonteams", "redditelementscoc", "tiapodcast", "militaryconspiracy", "letsplaymygame", "airguns", "conservativesuk", "iceandfirepowers", "reno", "exadventist", "optics", "testxfluffdawg", "2016elections", "fleshgait", "mariomakerlevels", "pensacola", "woodcarving", "femmethoughtsfeminism", "ripmerry", "killerinstinct", "onhub", "scipy", "clashroyalecirclejerk", "academicphilosophy", "stwnhms15ya", "twrp", "deathmetal", "summoners", "zooperwidget", "mozillainaction", "pixelatedbaloneywp", "aucklandbaconeaters", "greninjamains", "phonesexwithtodd", "romoadventureclub", "adultbreastfeeding", "uplay", "rpbleach", "skinallergies", "schizophreniaanxiety", "subredditpublicity", "blitzcrankmains", "mattswrittenword", "doodles", "rbnrelationships", "overwatch_ja", "thepeoplesbard", "xmage", "frozenproject", "cloprp", "kinky", "incampaign", "pamasich", "seireiteirp", "mid_century", "botrights", "carletonu", "frasier", "lighthouseprojects", "slingtv", "shoestring", "alpertlpinefiction", "justbrothings", "audiology", "industrialworldpowers", "hotwheels", "weccirclejerk", "construction", "onthisdateinbahai", "imdbfilmgeneral", "orchids", "adhd_anxiety", "israelpalestinefacts", "gamergatecopypasta", "transformerstrading", "fringescience", "giveme40days", "demohoi4legislature", "pathbrewer", "ktm", "bibleexegesis", "ifseniorclass", "psychedelics", "easymonsreference", "talesfromthemilitary", "breadwallet", "dacriawrites", "mysterysnails", "quant", "librarianknights", "ukskeptic", "goodshillhunting", "geekdfw", "filme", "drmariomains", "libya", "spongebob", "cf4cf", "hearthpacks", "holderclashers", "lawcanada", "collegeinfogeek", "colorists", "fifaclubs", "simplerocketssasa", "augusta", "jritslounge", "moneromarketing", "pogospoofing", "gascar", "nosleepaudio", "emetophobia", "bowsermains", "ketobabies", "wallpapers", "bynumbers", "atxgaybros", "newparents", "csgobettingtest", "zengmfootball", "brawlhallaclans", "thwipthwip", "exmormonen", "scarcade", "frozenfun", "modafinilbank", "findascoby", "evolutionreddit", "switch", "chocolatechipwp", "teamsesh", "hiphopimages", "test0324", "gottheories", "woiafpowers", "isidroid", "coc_redditoak", "sagesgrandarchives", "mynintendo", "factorio", "fearthewalkingdead", "programmingrequests", "southern_belle220", "tucker_carlson", "cadamus", "westbengal", "bengali", "step1", "houstonbeer", "zugorphans", "buildalinuxpc", "elementary", "thatsnobempire", "indianfood", "panamapapers", "ebwb", "carmodification", "portlandtrees", "gumdropgoober", "simpleios", "csgoweaponbalancemod", "blakester731", "john17999", "gtavcustoms", "conlangproject", "explainlikeimphd", "nin", "touhou_jp", "jayhawks", "augmentedreality", "mars", "titanfall_ctf", "chipcards", "chipotle", "sporecontest", "ecto", "vaperequests", "leagueofgiving", "vindictus", "esmereldaweatherwax", "see", "origami", "casemods", "dota2_jp", "dogdays", "psychonautreadingclub", "nocturnalwonderland", "mlslounge", "littlespacepersonals", "cfbball", "anw", "psp", "pokemonteams", "antivax", "bikeshop", "wesanderson", "quantikxanax", "protestant", "neutraltalk", "genderegalitarian", "gameaudio", "canning", "elint", "worststory", "cryptohardware", "rwcs", "botwallpaper", "cardistry", "zurich", "solving_qrzc", "interactivefiction", "lacrosse", "btcnewsfeed", "ocpresentation", "de_writingprompts", "exbahai", "wc2014", "expats", "longevity", "mmodesign", "pools", "dragon029", "software_ja", "taricmains", "firstdayontheinternet", "cnc", "mra", "britain", "jerma985", "coincidence", "sarkasticwatcher", "horrormoviechallenge", "transytalk", "marco_rubio", "owprotips", "feedmequickwriting", "lunchbreak_fiction", "danidvtest", "turcophobia", "subnautica", "transformation", "bifl", "djscirclejerk", "cultofdeadbones", "osuonlinecs", "starwarscanon", "mycastlefeeu", "pitchamovie", "modeltrains", "roaches", "oscars", "karmakourt", "diy_tech", "pixelblacksmith", "nirvanaschool", "communists", "cyberlaws", "intelnuc", "lincoln", "whatisthispainting", "afcwimbledon", "shittypopanalysis", "musicalchallenge", "mixedasians", "planetsidebattles", "talesfromelite", "libertyworldproblems", "bityard", "mariasmining", "thesilentforest", "openvpn", "merylrearsolid", "tachibana", "australiasim", "baofeng", "australiasimhouse", "magicdotp", "gtacrews", "openuniversity", "malesupportnetwork", "celsius232", "reddit_phoenix", "theexplorersguide", "prebiotics", "redpillworkplace", "pharmacology", "easports_nhl"]

df = pd.read_csv('soc-redditHyperlinks-body.tsv', sep='\t')  # Replace with your actual file path

# Ensure the 'source', 'target', and 'timestamp' columns exist (replace with your actual column names)
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])  # Convert 'timestamp' to datetime format
def CalcDegDiffAtTime(subreddit, time):
    start = 0
    starttime = time - timedelta(weeks=2)
    count = 0
    single = []
    single.append(subreddit)
    filtered_df1 = df[df['TARGET_SUBREDDIT'].isin(single)]
    for timestamp, group in filtered_df1.groupby('TIMESTAMP'):  
        if(time < timestamp):
            break
        if(starttime >= timestamp):
            start += 1
        count += 1
    return count - start


# Filter the data to include only the rows with the top 10 subreddits in either source or target
filtered_df = df[df['SOURCE_SUBREDDIT'].isin(top_25_subreddits)]
print("Rows after filtering:", filtered_df.shape[0])

# Create an empty list to store degree counts over time
degree_over_time = []
x = 0
y = 0
for timestamp, group in filtered_df.groupby('TIMESTAMP'):
    source = group["TARGET_SUBREDDIT"].tolist()[0]
    y += CalcDegDiffAtTime(source, timestamp + timedelta(weeks=2))
    x += 1
    if(x % 1000 == 0):
        print(x)


print(y)
print(y/x)



print(CalcDegDiffAtTime("askreddit", datetime(2015, 9, 1, 10, 30, 0)))












