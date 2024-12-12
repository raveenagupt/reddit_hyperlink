import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import json

def findInfectionTime(weight):
    if(weight >= 100):
        return 1
    ran = random.randint(-1,1)
    return 11 - (weight // 10) + ran


#df = pd.read_csv('test.tsv', sep='\t')
df = pd.read_csv('soc-redditHyperlinks-body.tsv', sep='\t')

G = nx.DiGraph()

for index, row in df.iterrows():
    source = row['SOURCE_SUBREDDIT']
    target = row['TARGET_SUBREDDIT']
    if(G.has_edge(source,target)):
        G[source][target]['weight'] += 1
        #G[source][target]['time'] = 5
    else:
        G.add_edge(source, target, weight=1)

top250 = ["askreddit", "iama", "pics", "writingprompts", "videos", "leagueoflegends", "todayilearned", "worldnews", "funny", "news", "nfl", "gaming", "relationships", "politics", "pcmasterrace", "soccer", "nba", "bitcoin", "adviceanimals", "dota2", "hockey", "subredditdrama", "the_donald", "explainlikeimfive", "mhoc", "movies", "anime", "technology", "globaloffensive", "kotakuinaction", "science", "conspiracy", "showerthoughts", "wtf", "dogecoin", "books", "gifs", "destinythegame", "outoftheloop", "buildapc", "android", "hearthstone", "games", "theredpill", "sandersforpresident", "nosleep", "legaladvice", "techsupport", "europe", "cfb", "tifu", "personalfinance", "fitness", "askhistorians", "changelog", "christianity", "smashbros", "magictcg", "askscience", "gonewildaudio", "modelusgov", "thesilphroad", "music", "dnd", "offmychest", "twoxchromosomes", "mildlyinteresting", "atheism", "electronic_cigarette", "starcitizen", "lifeprotips", "aww", "baseball", "soccerstreams", "dataisbeautiful", "india", "overwatch", "minecraft", "makeupexchange", "changemyview", "sysadmin", "bestof", "globaloffensivetrade", "darknetmarkets", "dirtypenpals", "drugs", "futurology", "jokes", "tumblrinaction", "trees", "sex", "whowouldwin", "entrepreneur", "gamesale", "dogemarket", "loseit", "wow", "squaredcircle", "pokemon", "elitedangerous", "pokemongo", "askmen", "gamerghazi", "canada", "oculus", "nofap", "collegebasketball", "testimonials", "casualiama", "clashofclans", "tagpro", "space", "relationship_advice", "malefashionadvice", "diy", "nottheonion", "unitedkingdom", "anarchism", "summonerschool", "worldbuilding", "history", "socialism", "civcraft", "mensrights", "television", "buildapcforme", "pokemongiveaway", "hiphopheads", "tf2", "footballhighlights", "tipofmytongue", "self", "ps4", "ratemymayor", "undelete", "steam", "de", "fireemblem", "49ers", "sf4", "anarcho_capitalism", "raisedbynarcissists", "depression", "buildapcsales", "asoiaf", "browns", "programming", "documentaries", "jailbreak", "planetside", "chargers", "pcgaming", "drama", "apple", "xboxone", "gamedev", "advice", "linux", "food", "mechanicalkeyboards", "pokemontrades", "windows10", "heroesofthestorm", "politicaldiscussion", "jaguars", "4chan", "starwars", "nfl_draft", "assistance", "conservative", "eve", "learnprogramming", "gamedeals", "subredditsimulator", "redditrequest", "chibears", "mls", "fallout", "eagles", "philosophy", "tennesseetitans", "askwomen", "rpg", "shitredditsays", "guns", "mhocpress", "enoughtrumpspam", "electronicmusic", "creepy", "australia", "respectthreads", "interestingasfuck", "ravens", "bluejacketsgwg", "poketradereferences", "podemos", "woahdude", "theoryofreddit", "newsokur", "subredditcancer", "oaklandraiders", "darksouls3", "asktransgender", "argentina", "mapporn", "smite", "dndbehindthescreen", "makeupaddiction", "colts", "panthers", "nostupidquestions", "cringeanarchy", "diablo", "photoshopbattles", "nygiants", "boardgames", "miamidolphins", "islam", "askdocs", "dndnext", "starcraft", "truereddit", "competitivehs", "buccaneers", "saints", "blackpeopletwitter", "seattle", "debatereligion", "cowboys", "me_irl", "karmacourt", "guildwars2", "buffalobills", "getmotivated", "sakuragakuin", "cars", "nyjets", "startups", "talesfromtechsupport", "thebutton", "bengals", "oldschoolcool", "unresolvedmysteries", "nvidia", "whatisthisthing", "skyrim", "motorcycles", "seahawks", "ultrahardcore", "denverbroncos", "pmsforsale", "texans", "keto", "sweden", "circlebroke", "detroitlions", "redskins", "fo4", "vive", "fantheories", "gameofthrones", "ethereum", "cigarmarket", "mindcrack", "suicidewatch", "thebluepill", "fantasy", "freeebooks", "confession", "spikes", "nhlstreams", "mylittlepony", "metalcore", "ama", "nootropics", "cmhoc", "azcardinals", "writing", "getdisciplined", "libertarian", "sports", "crucibleplaybook", "adhd", "investing", "skyrimmods", "math", "kpop", "imaginarydialogues", "amd", "2007scape", "nbastreams", "internetisbeautiful", "teenagers", "upliftingnews", "btc", "darksouls", "help", "casualconversation", "mylittleshellbullet17", "gwabackstage", "parenting", "ssbpm", "whowouldwinverse", "greenbaypackers", "grandtheftautov", "travel", "ukpolitics", "ironthronepowers", "twitch", "frugal", "circlejerk", "stock_picks", "gonewildstories", "rocketleague", "avsgwg", "toronto", "pokemonexchange", "yugioh", "exmormon", "competitiveoverwatch", "cringepics", "art", "france", "usefulscripts", "torontoevents", "syriancivilwar", "beercellar", "destinysherpa", "halo", "economics", "asksciencefiction", "catholicism", "psychonaut", "forhire", "ireland", "minnesotavikings", "guitar", "svexchange", "mma", "falcons", "nintendo", "acsbot", "makingamurderer", "manga", "dogs", "linuxquestions", "monsterhunter", "gwaprofiles", "redditclansystem", "civ", "crazyideas", "cscareerquestions", "nomansskythegame", "youshouldknow", "gamegrumps", "anime_irl", "meditation", "imgoingtohellforthis", "gaybros", "feminism", "ffxiv", "earthporn", "purplepilldebate", "steelers", "historyporn", "battlefield_4", "bicycling", "mlplounge", "soargaming", "formula1", "askgaybros", "theydidthemath", "pillowtalkaudio", "privacy", "runescape", "r4r", "femradebates", "cringe", "photography", "charitablebets", "badhistory", "bestof2015", "latestagecapitalism", "skincareaddiction", "darksouls2", "place", "jobs", "kansascitychiefs", "modernmagic", "newzealand", "reactiongifs", "3ds", "iphone", "roleplaygateway", "undertale", "askphilosophy", "kerbalspaceprogram", "babybumps", "unearthedarcana", "bindingofisaac", "mac", "running", "thedivision", "mcservers", "androidquestions", "fivenightsatfreddys", "serialpodcast", "feedthebeast", "paydaytheheist", "nsfw_gif", "fantasyfootball", "metal", "imaginarynetwork", "paranormal", "comicbooks", "european", "cryptocurrency", "exmuslim", "losangeles", "losangelesrams", "hfy", "trollxchromosomes", "portland", "mmorpg", "bodyweightfitness", "fashionreps", "lgbt", "lordsofminecraft", "china", "twitchplayspokemon", "trendingsubreddits", "linux4noobs", "netsec", "applehelp", "ygofeedback", "againsthatesubreddits", "austin", "quityourbullshit", "paradoxplaza", "occult", "cigars", "patriots", "webdev", "childfree", "mhoir", "realestatetechnology", "listentothis", "minecraftsuggestions", "languagelearning", "edmproduction", "beermoney", "suggestalaptop", "ketorecipes", "deadbedrooms", "networking", "lsd", "spacex", "pokemonplaza", "codcompetitive", "indieheads", "enoughlibertarianspam", "bitcoinmarkets", "raspberry_pi", "streetwear", "seduction", "onepiece", "capitalismvsocialism", "japan", "frozen", "androidapps", "nascar", "ffrecordkeeper", "dailyprogrammer", "truechristian", "latterdaysaints", "gadgets", "romania", "wearethemusicmakers", "python", "casualpokemontrades", "nflstreams", "oddlysatisfying", "truegaming", "learnpython", "iamverysmart", "geopolitics", "asianbeauty", "boston", "awwnime", "modsupport", "ironthronerp", "worldpolitics", "hailcorporate", "chicago", "c_s_t", "askengineers", "topmindsofreddit", "nofapchristians", "ploungemafia", "justneckbeardthings", "mechmarket", "trueanime", "belgium", "randomkindness", "okcupid", "mushroomkingdom", "monstercat", "weightroom", "anxiety", "femalefashionadvice", "london", "stevenuniverse", "freebies", "conspiratard", "buddhism", "glitch_in_the_matrix", "enhancement", "circlebroke2", "rage", "wiiu", "homelab", "frugalmalefashion", "srssucks", "talesfromretail", "uhcmatches", "pkmntcgreferences", "shortscarystories", "spam", "rocketleagueexchange", "dfsports", "hillaryclinton", "progresspics", "unexpected", "publicfreakout", "pokemongodev", "political_revolution", "asianamerican", "devoted", "thenetherlands", "gtaonline", "brasil", "shave_bazaar_feedback", "customhearthstone", "ideasfortheadmins", "fullcommunism", "millionairemakers", "zelda", "giftcardexchange", "pathofexile", "electromagnetics", "rickandmorty", "contestofchampions", "silverbugs", "bourbon", "mechanicadvice", "vegan", "badeconomics", "ssbm", "bitmarket", "gonewild", "wallstreetbets", "pathfinder_rpg", "blackops3", "pokeplazareferences", "forwardsfromgrandma", "harrypotter", "redditgetsdrawn", "buildmeapc", "arduino", "stlouisblues", "suity", "tiadiscussion", "footballdownload", "animesuggest", "marriedredpill", "nexus6p", "afl", "elderscrollsonline", "loleventvods", "needadvice", "nyc", "windows", "osugame", "civbattleroyale", "polandball", "mandelaeffect", "pac12", "worldwhisky", "musictheory", "conlangs", "askfeminists", "nofapwar", "mhol", "amiugly", "shitamericanssay", "medicine", "financialindependence", "metalgearsolid", "giftofgames", "incremental_games", "bloodborne", "debateachristian", "wredditstreams", "mgtow", "dating_advice", "announcements", "ticktockmanitowoc", "homeimprovement", "thathappened", "dragonage", "religion", "watches", "woodworking", "playark", "israel", "mhocgevotes", "negareddit", "windowsphone", "translator", "marvelstudios", "copypasta", "badphilosophy", "programmerhumor", "nintendoswitch", "osrstranscripts", "askelectronics", "playrust", "sexystories", "modelsouthernstate", "gameofthronesrp", "actuallesbians", "youtubehaiku", "survivor", "repsneakers", "youtube", "foreveralone", "buttcoin", "dota2trade", "atlanta", "germany", "bugs", "mormon", "tinder", "3dprinting", "rant", "italy", "asktrumpsupporters", "gangstalking", "blog", "iosthemes", "ethtrader", "houston", "bodybuilding", "laexploratorybrigade", "unity3d", "washingtondc", "askanamerican", "wikileaks", "tmobile", "joinrobin", "marketing", "csgobetting", "lfg", "amiibo", "witcher", "ecigclassifieds", "goodyearwelt", "ainbow", "bestofoutrageculture", "comics", "clashroyale", "roosterteeth", "asktrp", "daddit", "mildlyinfuriating", "dogecoinbeg", "military", "needamod", "electronics", "thelastairbender", "londonsocialclub", "h1z1", "tna", "beer", "blackout2015", "linux_gaming", "marvel", "redditdev", "eatcheapandhealthy", "mltp", "shittyaskscience", "debateanarchism", "posthardcore", "dayz", "edh", "yogscast", "summonerswar", "dankmemes", "vancouver", "dogemining", "subredditads", "cooking", "askacademia", "powerlifting", "redditzulucoc", "socialskills", "startrek", "civilizatonexperiment", "wayofthebern", "mentalhealth", "bostonceltics", "physics", "fireteams", "engineering", "battlestations", "kanye", "denmark", "uncensorednews", "bdsmcommunity", "blackladies", "eltp", "yalit", "excel", "facepalm", "xxfitness", "linuxadmin", "hockeygamegifs", "hardware", "sanfrancisco", "srsdiscussion", "reddevils", "gwascriptguild", "netflix", "samplesize", "supremeclothing", "learndota2", "masseffect", "actrade", "niceguys", "overwatchuniversity", "custommagic", "vaporents", "russia", "onions", "flexibility", "streetfighter", "smallbusiness", "modhelp", "oneplus", "speedrun", "mbti", "crappydesign", "archlinux", "ggfreeforall", "hongkong", "menslib", "aquariums", "chrome", "osx", "homebrewing", "morbidreality", "justiceporn", "titanfall", "intp", "hotwife", "scotland", "web_design", "rbi", "korea", "redditnemesis", "test", "audiophile", "procss", "lostgeneration", "wardrobepurge", "canadapolitics", "stopdrinking", "scfeedback", "formerfutureauthor", "ocpoetry", "randomactsofgaming", "sorceryofthespectacle", "liverpoolfc", "infj", "redpillwomen", "gendercritical", "shadowban", "grandtheftautov_pc", "androidgaming", "multicopter", "indiegaming", "babymetal", "vexillology", "arma", "dogestarter", "cats", "datahoarder", "mexico", "flashtv", "cynicalbrit", "arrow", "csshelp", "collapse", "ncaaw", "dirtyr4r", "quebec", "truefilm", "rupaulsdragrace", "gtaglitches", "jontron", "asianmasculinity", "surface", "kappa", "hacking", "redditecho", "montreal", "scotch", "battlefield", "ask_politics", "whiskyporn", "asksocialscience", "crusaderkings", "sacfood", "targetedenergyweapons", "incest", "kratom", "philippines", "teslore", "airsoft", "plex", "rainbow6", "vinyl", "agmarketplace", "highqualitygifs", "h3h3productions", "homemadexxx", "falloutmods", "hcteams", "intj", "turkey", "againstgamergate", "foodporn", "engineeringstudents", "lakers", "opiates", "arabs", "frankocean", "hapas", "iwantout", "rcsources", "nltp", "researchchemicals", "basicincome", "fatlogic", "sydney", "aspergers", "litecoin", "diy_ejuice", "workersvanguard", "clashofclansmu", "askculinary", "animesakuga", "eu4", "gainit", "wet_shavers", "radiohead", "rwby", "melbourne", "lewronggeneration", "markmywords", "unixporn", "randomactsofblowjob", "raidsecrets", "communism", "diablo3", "standupshots", "roastme", "dogeducation", "skincareexchange", "metaphotography", "randomactsofmuffdive", "pornvids", "climbing", "audiocandy", "oppression", "skeptic", "fifa", "worldpowers", "homenetworking", "cordcutters", "wildhockey", "protectandserve", "bestof2014", "blinkpool", "holdthemoan", "cubers", "asianbeautyexchange", "ukrainianconflict", "iran", "campingandhiking", "gundeals", "linguistics", "90daysgoal", "pornfree", "itrpcommunity", "iranian", "nexus5x", "danknation", "loans", "cricket", "hxh_oc", "narutobattlegrounds", "rmmorpgdiscussions", "schoolidolfestival", "the_dvls_advocate", "singapore", "nexus5", "sto", "ukraina", "army", "askuk", "modelcentralstate", "dccomics", "neverbegameover", "resissues", "findareddit", "karmacourtblog", "chicagobulls", "luciddreaming", "gunners", "starcitizen_trades", "fearme", "gundam", "fakeid", "teslamotors", "stobuilds", "smitegodconcepts", "fifacoins", "elitelavigny", "warframe", "finalfantasy", "photoshoprequest", "dbz", "headphones", "gbftradereference", "ubuntu", "random_acts_of_pizza", "swagbucks", "nsfw", "whiskyinventory", "dropinfootball", "letsnotmeet", "gardening", "africa", "learnjapanese", "codzombies", "whisky", "churning", "kohi", "google", "pokemonforall", "pakistan", "eliteantal", "whatcouldgowrong", "calgary", "mariomaker", "hunterxhunter", "xcom", "dota2loungebets", "justnomil", "creepypms", "newsokunomoral", "3dshacks", "answers", "rainmeter", "dallas", "coins4sale", "weddingplanning", "modnews", "polyamory", "furry", "doctorwho", "newsokurmod", "ygosales", "naruto", "againstmensrights", "starwarsbattlefront", "watchinganime", "altright", "dncleaks", "pubtips", "warthunder", "randomactsofchristmas", "santaslittlehelpers", "literature", "murica", "iwanttolearn", "scifi", "playmygame", "punchablefaces"]

timetogiant = []

for ind in range(1000):
    if(ind % 10 == 0):
        print('hi')
    # Set initial infected nodes (can be modified)
    initial_infected = []
    initial_infected.append(top250[ind])  # Example of starting infected nodes

    # Initialize node states: S = susceptible, I = infected
    node_states = {node: 'S' for node in G.nodes}
    for node in initial_infected:
        node_states[node] = 'I'

    # Create a dictionary to store the time when nodes will become infected
    infection_times = {node: -1 for node in G.nodes}

    # Set the initial infected nodes to time 0
    for node in initial_infected:
        infection_times[node] = 0

    # Simulation parameters
    max_timesteps = 250  # You can set this to any value based on your simulation needs
    timesteps = 0

    # List to track the number of infected nodes at each timestep
    infected_counts = []
    i = 0
    # Run the SI model
    while timesteps < max_timesteps:
        # Track the number of infected nodes at this timestep
        infected_count = sum(1 for state in node_states.values() if state == 'I')
        infected_counts.append(infected_count)

        # Go through each node to check for infection spread
        for node in G.nodes:
            if node_states[node] == 'I':
                # This node is infected, check its neighbors
                for neighbor in G.predecessors(node):
                    if node_states[neighbor] == 'S' and infection_times[neighbor] == -1:
                        # Calculate the infection time based on the weight of the edge
                        edge_weight = G[neighbor][node]['weight']

                        if(infection_times[neighbor] == -1):
                            time_to_infect = findInfectionTime(edge_weight)
                        
                            # If the neighbor has not been infected earlier or can be infected now
                            infection_times[neighbor] = timesteps + time_to_infect

        # Increment timestep
        timesteps += 1
        
        # Update the node states based on the infection times
        for node in G.nodes:
            if node_states[node] == 'S' and infection_times[node] != -1 and infection_times[node] <= timesteps:
                node_states[node] = 'I'
                i += 1
        if(i >= 25500):
            timetogiant.append(timesteps)
            break

with open("upper_25_subreddits.json", "w") as file:
    json.dump(timetogiant, file)

xvalues = np.arange(998)
yvalues = timetogiant

plt.plot(xvalues, yvalues)
plt.xlabel('Subreddit Rank')
plt.ylabel('TimeSteps')
plt.title('TimeSteps to Infect Giant Component')
plt.grid(True)
plt.show()