import asyncio
import genshin


# async def create_client(ltuid:int, ltoken:str):
async def create_hk4e(account_id:int, cookie_token:str):
    cookies = locals()
    client = genshin.Client(cookies, game=genshin.Game.GENSHIN)
    return client

async def create_hkrpg(account_id:int, cookie_token:str):
    cookies = locals()
    client = genshin.Client(cookies, game=genshin.Game.STARRAIL)
    return client

async def redeem_code(client:genshin.Client, promo="", **qwargs): # type: ignore
    # redeem a gift code for the currently logged-in user
    await client.redeem_code(promo, **qwargs)


async def claim_rewards(client:genshin.Client):
    # claim daily reward
    try:
        reward = await client.claim_daily_reward(reward=False)
        print(f"Claimed {reward.amount}x {reward.name}") # type: ignore
    except genshin.AlreadyClaimed:
        print("Daily reward already claimed")

    # get all claimed rewards
    # async for reward in client.claimed_rewards():
    #    print(f"{reward.time} - {reward.amount}x {reward.name}")

    # get info about the current daily reward status
    signed_in, claimed_rewards = await client.get_reward_info()
    print(f"Signed in: {signed_in} | Total claimed rewards: {claimed_rewards}")
    return 0


async def main():
    client = await create_hkrpg(2, "")
    # client = await create_hk4e(2, "")
    _res = await claim_rewards(client) #; exit()
    # print(await client.get_game_accounts()); exit()
    await client.redeem_code(
        code="",
        # game_biz : str = "hk4e_global"
        # game_biz="hkrpg_global", 
        )



if __name__ == '__main__':
    asyncio.run(main())