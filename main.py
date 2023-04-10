################  REQUIRED LIBRARIES ####################

from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import config

##############  LOAD PLAYER PEFORMANCE ##################

player_df = pd.read_csv(config.CSV_FILE_PATH)

################# FLASK Application #####################

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

################## API FOR Openers Batters ######################

@app.route('/first')
def first():
    return render_template('opener.html')

@app.route('/opener')        
def open():

    a = eval(request.args.get('a'))                                   # request inputs
    b = eval(request.args.get('b'))
    c = eval(request.args.get('c'))
    d = eval(request.args.get('d'))
    e = eval(request.args.get('e'))

    openers = player_df.loc[(player_df['batting_Avg'] > c) & (player_df['str_rate'] > d) & (player_df['innings'] > b) & (player_df['boundry%'] > e) & (player_df['bat_pos'] < a)]
    openers = openers[['name','contry','battingStyle','innings','indivisual_runs','total_balls','str_rate','batting_Avg','bat_pos','boundry%']]
 
    openers.to_html('templates//df.html')                            # df after appling above filters saved to html, this html page will be displayed in final result page


    plt.figure(figsize= (12,4))                                     # data visualization
    plt.subplot(1,2,1)
    plt.title('Runs Scored')
    sns.barplot(y = 'name' , x = 'indivisual_runs', data = openers, palette = 'rainbow_r', orient = 'h')
    plt.subplot(1,2,2)
    plt.title('Average Run Vs Strike Rate')
    sns.scatterplot(x = 'batting_Avg', y = 'str_rate', data = openers, hue = 'name', s = 300,palette = 'rainbow_r')
    plt.legend(markerscale = 2)
    sns.set(style = 'whitegrid')
    plt.savefig('templates//img1.png')                             # plots saved to image, this image will be displayed in final result page


    return render_template('result.html')


################## API FOR MIDDLE ORDER ######################

@app.route('/second')
def second():
    return render_template('middle.html')

@app.route('/middle')              
def middle():
    a = eval(request.args.get('a'))
    b = eval(request.args.get('b'))
    c = eval(request.args.get('c'))
    d = eval(request.args.get('d'))
    e = eval(request.args.get('e'))


    middle = player_df.loc[(player_df['batting_Avg'] > c) & (player_df['str_rate'] > d) & 
              (player_df['innings'] > b) & (player_df['avg_balls'] > e) &
             (player_df['bat_pos'] > a)]
    middle = middle[['name','contry','battingStyle','innings','indivisual_runs','total_balls','str_rate','batting_Avg','bat_pos','boundry%','avg_balls']]
 
    middle.to_html('templates//df.html')


    plt.figure(figsize= (12,4))
    plt.subplot(1,2,1)
    plt.title('Runs Scored')
    sns.barplot(y = 'name' , x = 'indivisual_runs', data = middle, palette = 'rainbow_r', orient = 'h')
    plt.subplot(1,2,2)
    plt.title('Average Runs Vs Strike Rate')
    sns.scatterplot(x = 'batting_Avg', y = 'str_rate', data = middle, hue = 'name', s = 300,palette = 'rainbow_r')
    plt.legend(markerscale = 2)
    sns.set(style = 'whitegrid')

    plt.savefig('templates//img1.png')


    return render_template('result.html')

################## API FOR LOWER ORDER ######################

@app.route('/third')
def third():
    return render_template('lower.html')

@app.route('/lower')              
def finisher():
    a = eval(request.args.get('a'))
    b = eval(request.args.get('b'))
    c = eval(request.args.get('c'))
    d = eval(request.args.get('d'))
    e = eval(request.args.get('e'))
    f = eval(request.args.get('f'))


    finisher = player_df.loc[(player_df['batting_Avg'] > c) & (player_df['str_rate'] > d) & (player_df['innings'] > b) & (player_df['avg_balls'] > e) & (player_df['bat_pos'] >= a) &(player_df['innings_bowled'] > f)]
    
    finisher = finisher[['name','contry','battingStyle','bowlingStyle','innings_bowled','innings','indivisual_runs','bow_avg','batting_Avg','str_rate','bat_pos','innings_bowled','wickets','bow_economy','Bow_strike_rate']] 
    
    finisher.to_html('templates//df.html')


    plt.figure(figsize= (12,4))
    plt.subplot(1,2,1)
    plt.title('Runs Scored')
    sns.barplot(y = 'name' , x = 'indivisual_runs', data = finisher, palette = 'rainbow_r', orient = 'h')
    plt.subplot(1,2,2)
    plt.title('Average Runs Vs Strike Rate')
    sns.scatterplot(x = 'batting_Avg', y = 'str_rate', data = finisher, hue = 'name', s = 300,palette = 'rainbow_r')
    plt.legend(markerscale = 2)
    sns.set(style = 'whitegrid')

    plt.savefig('templates//img1.png')


    return render_template('result.html')

################## API FOR Allrounder ######################

@app.route('/fourth')
def fourth():
    return render_template('allrounder.html')

@app.route('/allrounder')              
def rounder():
    a = eval(request.args.get('a'))
    b = eval(request.args.get('b'))
    c = eval(request.args.get('c'))
    d = eval(request.args.get('d'))
    e = eval(request.args.get('e'))
    f = eval(request.args.get('f'))
    g = eval(request.args.get('g'))


    allrounder = player_df.loc[(player_df['batting_Avg'] > c) & (player_df['str_rate'] > d) & (player_df['innings'] > b) & (player_df['bow_economy'] < f) & (player_df['bat_pos'] > a) &(player_df['innings_bowled'] > e) & (player_df['Bow_strike_rate'] < g)]

    allrounder = allrounder[['name','contry','battingStyle','bowlingStyle','innings','indivisual_runs','batting_Avg','str_rate','bat_pos','innings_bowled','bow_avg','innings_bowled','wickets','bow_economy','Bow_strike_rate']]

    allrounder.to_html('templates//df.html')

    plt.figure(figsize= (15,4))
    plt.subplot(1,4,1)
    plt.title('Runs Scored')
    sns.barplot(y = 'name' , x = 'indivisual_runs', data = allrounder, palette = 'rainbow_r', orient = 'h')
    plt.subplot(1,4,2)
    plt.title('Wickets')
    sns.barplot(y = 'name' , x = 'wickets', data = allrounder, palette = 'rainbow_r', orient = 'h')
    plt.subplot(1,4,3)
    plt.title('Batting Avg Vs Strike Rate')
    sns.scatterplot(x = 'batting_Avg', y = 'str_rate', data = allrounder, hue = 'name', s = 300,palette = 'rainbow_r')
    plt.subplot(1,4,4)
    plt.title('Bowling Economy Vs Strike Rate')
    sns.scatterplot(x = 'Bow_strike_rate', y = 'bow_economy', data = allrounder, hue = 'name', s = 300,palette = 'rainbow_r')
    plt.legend(markerscale = 2)
    sns.set(style = 'whitegrid')

    plt.savefig('templates//img1.png')

    return render_template('result.html')


################## API FOR Fast Bowler ######################

@app.route('/fifth')
def fifth():
    return render_template('faster.html')

@app.route('/bowler')              
def faster():
    a = eval(request.args.get('a'))
    b = eval(request.args.get('b'))
    c = eval(request.args.get('c'))
    d = eval(request.args.get('d'))


    faster = player_df.loc[(player_df['innings_bowled'] > d) & (player_df['bow_economy'] < a) & 
              (player_df['Bow_strike_rate'] < b) &
            (player_df['bowlingStyle'].isin(['Right arm Medium fast','Right arm Fast medium','Right arm Fast','Left arm Fast medium','Left arm Medium fast','Left arm Fast','Right arm Medium fast, Right arm Offbreak'])) &
             (player_df['dot_ball_%'] > c)]
    
    faster = faster[['name','contry','bowlingStyle','innings_bowled','balls_bowled','runs_consided','wickets',
                 'bow_economy','bow_avg','Bow_strike_rate','dot_ball_%','maidens']]
    
    faster.to_html('templates//df.html')

    
    plt.figure(figsize= (12,4))
    plt.subplot(1,2,1)
    plt.title('Wickets')
    sns.barplot(y = 'name' , x = 'wickets', data = faster, palette = 'rainbow_r', orient = 'h')
    plt.subplot(1,2,2)
    plt.title('Economy Vs Strike Rate')
    sns.scatterplot(x = 'Bow_strike_rate', y = 'bow_economy', data = faster, hue = 'name', s = 300,palette = 'rainbow_r')
    plt.legend(markerscale = 2)
    sns.set(style = 'whitegrid')

    plt.savefig('templates//img1.png')

    return render_template('result.html')


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER)
