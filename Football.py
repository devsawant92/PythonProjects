
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[2]:


events = pd.read_csv('events.csv')


# In[3]:


event_type= {
    0:'Announcement',
1:'Attempt',
2:'Corner',
3:'Foul',
4:'Yellow card',
5:'Second yellow card',
6:'Red card',
7:'Substitution',
8:'Free kick won',
9:'Offside',
10:'Hand ball',
11:'Penalty conceded'
}

event_type2 = {
12:'Key Pass',
13:'Failed through ball',
14:'Sending off',
15:'Own goal'
}

side ={
1:'Home',
2:'Away'  
   }

shot_place = {
1 : 'Bit too high',
2 :'Blocked',
3 :'Bottom left corner',
4 :'Bottom right corner',
5 : 'Centre of the goal',
6 : 'High and wide',
7 : 'Hits the bar',
8 : 'Misses to the left',
9 : 'Misses to the right',
10 : 'Too high',
11 :'Top centre of the goal',
12 :'Top left corner',
13 :'Top right corner'

}


shot_outcome = {
1:'On target',
2:'Off target',
3:'Blocked',
4:'Hit the bar',
}
    
location = {
1:'Attacking half',
2:'Defensive half',
3:'Centre of the box',
4:'Left wing',
5:'Right wing',
6:'Difficult angle and long range',
7:'Difficult angle on the left',
8:'Difficult angle on the right',
9:'Left side of the box',
10:'Left side of the six yard box',
11:'Right side of the box',
12:'Right side of the six yard box',
13:'Very close range',
14:'Penalty spot',
15:'Outside the box',
16:'Long range',
17:'More than 35 yards',
18:'More than 40 yards',
19:'Not recorded'

}


bodypart = {
1:'right foot',
2:'left foot',
3:'head'
}

assist_method = {
0:'None',
1:'Pass',
2:'Cross',
3:'Headed pass',
4:'Through ball'
}

situation = {
1:'Open play',
2:'Set piece',
3:'Corner',
4:'Free kick'
   
}  


# In[4]:


events.event_team.unique()


# In[5]:


seria_a = ['Napoli','Juventus','Siena','Atalanta','Bastia','Catania','Genoa','AC Milan',
           'Palermo','Internazionale','Parma','AS Roma','Cagliari','Fiorentina','Bologna',
           'Lazio','Udinese','Sampdoria','Torino','Livorno','Empoli','Chievo Verona','Novara',
           'US Pescara','Hellas Verona','Frosinone','Carpi','Sassuolo','Cesena','Lecce','Crotone']

Bundesliga= ['Hamburg SV','Borussia Dortmund','FC Augsburg','SC Freiburg','Werder Bremen',
             'Borussia Monchengladbach','Bayern Munich','Bayer Leverkusen','Eintracht Frankfurt',
             'TSV Eintracht Braunschweig','Hertha Berlin','VfB Stuttgart','Schalke 04',
            'Hannover 96','RB Leipzig','VfL Wolfsburg','Nurnberg','FC Cologne',
             'Fortuna Dusseldorf','SV Darmstadt 98','TSG Hoffenheim','Kaiserslautern',
             'SpVgg Greuther Furth','FC Ingolstadt 04','SC Paderborn', 'Mainz']

LigaBBVA = ['Sporting Gijon','Real Madrid','Rayo Vallecano','Atletico Madrid','Barcelona',
            'Real Sociedad','Real Zaragoza','Athletic Bilbao','Espanyol','Valencia','Sevilla',
            'Getafe','Mallorca','Racing Santander','Malaga', 'Levante','Villarreal','Osasuna',
            'Deportivo La Coruna','Granada','Real Betis','Alaves','Real Valladolid','Celta Vigo',
            'Cordoba','Leganes','Las Palmas','Almeria','Elche','Eibar']

PremierlLeague =[ 'Aston Villa','Sunderland','Everton','West Brom','Norwich City','Leicester City','Hull',
                'Manchester Utd','Manchester City','Arsenal','Swansea','Burnley','Bournemouth','Fulham','Liverpool',
                'Newcastle','West Ham','Southampton','Tottenham','Stoke City','Crystal Palace','Cardiff','Chelsea',
                'QPR','Middlesbrough','Watford']

Ligue_1=['Paris Saint-Germain','Bordeaux','Lille','Nice','Toulouse','Lyon','Montpellier','St Etienne','AS Monaco',
         'Stade de Reims', 'Marseille','AS Nancy Lorraine','Valenciennes','Evian Thonon Gaillard','GFC Ajaccio',
         'Stade Rennes','AJ Auxerre','Brest','Caen','Lorient','AC Ajaccio','Sochaux','Dijon FCO',
         'Guingamp','Troyes','Nantes','Metz','Lens','Angers']


# In[6]:


def leagueMapping(data):
    if data in seria_a:
        return 'seria_a'
    if data in Bundesliga:
        return 'Bundesliga'
    if data in LigaBBVA:
        return 'LigaBBVA'
    if data in PremierlLeague:
        return 'PremierlLeague'
    if data in Ligue_1:
        return 'Ligue_1'


# In[7]:


events['league']= events['event_team'].apply(leagueMapping)


# In[8]:


events['event_type']= events['event_type'].map(event_type)
events['event_type2']= events['event_type2'].map(event_type2)
events['side']= events['side'].map(side)
events['shot_place']= events['shot_place'].map(shot_place)
events['shot_outcome']= events['shot_outcome'].map(shot_outcome)
events['location']= events['location'].map(location)
events['bodypart']= events['bodypart'].map(bodypart)
events['assist_method']= events['assist_method'].map(assist_method)
events['situation']= events['situation'].map(situation)


# In[9]:


events.head()


# In[10]:


TotalGoals = events[events['is_goal'] == True].groupby('time').size().reset_index(name='counts')
premierLeagueGoals = events[(events['is_goal'] == True) & (events['league']== 'PremierlLeague')].groupby('time').size().reset_index(name='counts')
BundesligaGloals = events[(events['is_goal'] == True) & (events['league']== 'Bundesliga')].groupby('time').size().reset_index(name='counts')
LigaBBVAGoals =  events[(events['is_goal'] == True) & (events['league']== 'LigaBBVA')].groupby('time').size().reset_index(name='counts')
Ligue_1Goals = events[(events['is_goal'] == True) & (events['league']== 'Ligue_1')].groupby('time').size().reset_index(name='counts')
seria_aGoals = events[(events['is_goal'] == True) & (events['league']== 'seria_a')].groupby('time').size().reset_index(name='counts')


# In[11]:


plt.figure(figsize=(20,10))
plt.subplot(211)
plt.xlabel("Time")
plt.ylabel("Number of Goals at Time")

plt.plot(premierLeagueGoals.time,premierLeagueGoals.counts,'r',linewidth=2)

plt.plot(BundesligaGloals.time,BundesligaGloals.counts,'b',linewidth=2)

plt.plot(LigaBBVAGoals.time,LigaBBVAGoals.counts,'k',linewidth=2)

plt.plot(Ligue_1Goals.time,Ligue_1Goals.counts,'m',linewidth=2)

plt.plot(seria_aGoals.time,seria_aGoals.counts,'c',linewidth=2)
plt.legend(['Premier League','Bundesliga','LigaBBVA','Ligue_1','seria_a'])
plt.grid(True)
plt.xticks(np.arange(0, 121, 10))

plt.subplot(212)

plt.plot(TotalGoals.time,TotalGoals.counts,linewidth=2)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Number of Goals at Time")
plt.xticks(np.arange(0, 121, 10))


# In[12]:


premierLeagueGoalsSituation = events[(events['is_goal'] == True) & (events['league']== 'PremierlLeague')].groupby('situation').size().reset_index(name='counts')
BundesligaGloalsSituations = events[(events['is_goal'] == True) & (events['league']== 'Bundesliga')].groupby('situation').size().reset_index(name='counts')
LigaBBVAGoalsSituations=  events[(events['is_goal'] == True) & (events['league']== 'LigaBBVA')].groupby('situation').size().reset_index(name='counts')
Ligue_1GoalsSituations = events[(events['is_goal'] == True) & (events['league']== 'Ligue_1')].groupby('situation').size().reset_index(name='counts')
seria_aGoalsSituations = events[(events['is_goal'] == True) & (events['league']== 'seria_a')].groupby('situation').size().reset_index(name='counts')


# In[13]:


plt.subplot(321)

plt.pie(premierLeagueGoalsSituation.counts,  labels=premierLeagueGoalsSituation.situation, 
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Premier League')
plt.subplot(322)

plt.pie(BundesligaGloalsSituations.counts,  labels=BundesligaGloalsSituations.situation, 
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Bundesliga')
plt.subplot(323)

plt.pie(LigaBBVAGoalsSituations.counts,  labels=LigaBBVAGoalsSituations.situation, 
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('LigaBBVA')
plt.subplot(324)

plt.pie(Ligue_1GoalsSituations.counts,  labels=Ligue_1GoalsSituations.situation, 
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Ligue_1')
plt.subplot(325)

plt.pie(seria_aGoalsSituations.counts,  labels=seria_aGoalsSituations.situation, 
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('seria a')


# In[14]:


RedCards = events[(events['event_type'] == 'Red card') | (events['event_type'] == 'Second yellow card') ].groupby('time').size().reset_index(name='counts')


# In[15]:



plt.plot(RedCards.time,RedCards.counts,linewidth=2)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Number of Goals at Time")
plt.xticks(np.arange(0, 121, 10))


# In[16]:


RedCards = events[(events['event_type2'] == 'Sending off') ].groupby('time').size().reset_index(name='counts')


# In[17]:


plt.plot(RedCards.time,RedCards.counts,linewidth=2)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Number of Red cards at Time")
plt.xticks(np.arange(0, 121, 10))


# In[18]:


eventspen= events[(events['event_type'] == 'Penalty conceded') ].groupby('time').size().reset_index(name='counts')


# In[19]:


plt.plot(eventspen.time,eventspen.counts,linewidth=2)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Number of penlty conceded at time")
plt.xticks(np.arange(0, 121, 10))

