import streamlit.web.cli as stcli
import sys


def streamlit_run():
    sys.argv = [
        "streamlit",
        "run",
        "AutoTeamBalancerWebApp.py",
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())


if __name__ == "__main__":
    streamlit_run()
