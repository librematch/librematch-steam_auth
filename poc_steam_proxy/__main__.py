import asyncio


def main():
    from __init__ import run

    try:
        asyncio.run(run())
    except (KeyboardInterrupt, RuntimeError):
        print("Goodbye...")
    pass


if __name__ == "__main__":
    main()
