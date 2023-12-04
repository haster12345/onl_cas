from Payouts import payout_classification
from Payouts import Payout
from Slot_Machine import SlotMachine
from flask import Flask
from flask import request, escape

app = Flask(__name__)


@app.route("/")
def index():
    n = str((request.args.get('number of symbols', 3)))
    payout = str(main(n)['payout'])

    return ("""<form action="" method="get">
                Number of symbols: <input type="text" name="n">
                <input type="submit" value="Spin!">
              </form>"""
            + 'Payout: '
            + payout
            )


def main(n, iterations=False, counter=1000):
    """ Spin for jackpot!"""
    n = int(n)

    try:
        symbols = SlotMachine(n).symbol_picker()
        payout_class = payout_classification(symbols)
        if iterations:
            iter = counter
            counter = iter
            for i in range(iter):
                counter += Payout(n).payout_main(payout_class)
            return counter

        # return (str(symbols), str(Payout(n).payout_main(payout_class)))
        return {'symbols': str(symbols), 'payout': str(Payout(n).payout_main(payout_class))}
    except ValueError:
        return 'Invalid Input'


if __name__ == '__main__':
    # n = 5
    # counter = 1000
    # print(main(n, False, counter))

    app.run(host="127.0.0.1", port=8080, debug=True)
