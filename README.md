# genshin.py

[![Downloads](https://pepy.tech/badge/genshin)](https://pepy.tech/project/genshin)
[![PyPI package](https://img.shields.io/pypi/v/genshin)](https://pypi.org/project/genshin/)
[![Last Commit](https://img.shields.io/github/last-commit/thesadru/genshin.py)](https://github.com/thesadru/genshin.py/commits/master)
[![Coverage](https://img.shields.io/codeclimate/coverage/thesadru/genshin.py)](https://codeclimate.com/github/thesadru/genshin.py)
[![Discord](https://img.shields.io/discord/570841314200125460?color=7289DA)](https://discord.gg/sMkSKRPuCR)

Modern API wrapper for Genshin Impact & Honkai Impact 3rd built on asyncio and pydantic.

---

Documentation: https://thesadru.github.io/genshin.py

API Reference: https://thesadru.github.io/genshin.py/pdoc/genshin

Source Code: https://github.com/thesadru/genshin.py

---

The primary focus of genshin.py is convenience. The entire project is fully type-hinted and abstracts a large amount of the api to be easier to use.

Key features:

- All data is in the form of Pydantic Models which means full autocompletion and linter support.
- Requests are significantly faster thanks to proper usage of asyncio.
- Chinese and Engrish names returned by the API are renamed to simpler English fields.
- Supports the majority of the popular endpoints.
- Cleanly integrates with frameworks like FastAPI out of the box.

> Note: This library is a successor to [genshinstats](https://github.com/thesadru/genshinstats) - an unofficial wrapper for the Genshin Impact api.

## Requirements

- Python 3.8+
- aiohttp
- Pydantic

```console
pip install genshin
```

## Example

A very simple example of how genshin.py would be used:

```py
import asyncio
import genshin


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
        )


if __name__ == '__main__':
    asyncio.run(main())
```

## Contributing

Any kind of contribution is welcome.
Please read [CONTRIBUTING.md](./CONTRIBUTING.md) to see what you need to do to make a contribution.
