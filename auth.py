from stake import StakeClient, SessionTokenLoginRequest, CredentialsLoginRequest
from dotenv import load_dotenv
load_dotenv()
import os
import asyncio
import webbrowser
import json

class Session:
    login_request = SessionTokenLoginRequest()
    if not login_request:
        login_request = CredentialsLoginRequest(
            username=os.environ.get('STAKE_USER'),
            password=os.environ.get('STAKE_PASS')
        )
    stake_session = StakeClient(login_request)
    os.environ['STAKE_TOKEN'] = stake_session.headers.stake_session_token
    print(json.dumps(stake_session.headers))
    print(os.environ.get('STAKE_TOKEN'))

async def print_user():
    async with StakeClient() as stake_session:
        print(stake_session.user.first_name)
        print(stake_session.headers.stake_session_token)

async def show_portfolio():
    async with StakeClient() as stake_session:
        equities = await stake_session.equities.list()
        for equity in equities.equity_positions:
            print(equity.symbol, equity.yearly_return_value)
        return equities
