import csv
import random
from datetime import datetime, timedelta

random.seed(42)

# 1. Generate igaming_players.csv (5,000 Players)
countries = ['CY', 'DE', 'UK', 'BR', 'CA', 'SE']
country_weights = [10, 25, 25, 20, 10, 10]
channels = ['Affiliate', 'Organic', 'Paid Social', 'PPC']
channel_weights = [40, 20, 25, 15]
start_reg_date = datetime(2025, 1, 1)

player_ids = list(range(10001, 15001))

with open('igaming_players.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['PLAYER_ID', 'COUNTRY_CODE', 'ACQUISITION_CHANNEL', 'REGISTRATION_DATE'])
    for pid in player_ids:
        country = random.choices(countries, weights=country_weights, k=1)[0]
        channel = random.choices(channels, weights=channel_weights, k=1)[0]
        reg_date = (start_reg_date + timedelta(days=random.randint(0, 364))).strftime('%Y-%m-%d')
        writer.writerow([pid, country, channel, reg_date])

# 2. Generate igaming_bets.csv (50,000 Bets)
categories = ['Slots', 'Live Casino', 'Sportsbook', 'Table Games']
cat_weights = [50, 20, 20, 10]
start_bet_date = datetime(2025, 6, 1)

with open('igaming_bets.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['BET_ID', 'PLAYER_ID', 'GAME_CATEGORY', 'BET_DATE', 'STAKE_EUR', 'WIN_EUR', 'BONUS_COST_EUR'])
    for bet_id in range(500001, 550001):
        pid = random.choice(player_ids)
        category = random.choices(categories, weights=cat_weights, k=1)[0]
        bet_date = (start_bet_date + timedelta(days=random.randint(0, 180))).strftime('%Y-%m-%d')
        
        stake = round(random.expovariate(1.0 / 25.0) + 1.0, 2)
        is_win = 1 if random.random() < 0.32 else 0
        multiplier = random.uniform(1.2, 4.5)
        win_amount = round(stake * is_win * multiplier, 2)
        bonus_used = round(stake * 0.2, 2) if random.random() < 0.15 else 0.0
        
        writer.writerow([bet_id, pid, category, bet_date, stake, win_amount, bonus_used])

print("SUCCESS: Generated igaming_players.csv and igaming_bets.csv!")