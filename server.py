from flask import Flask, json
import random

api = Flask(__name__)

current_metric = 0

@api.route('/metrics', methods=['GET'])
def get_metrics():
  value1 = random.random()
  value2 = random.random()
  return "# HELP some_metric is some metric\n# TYPE some_metric counter\nsome_metric {}\n# HELP some_other_metric too\n# TYPE some_other_metric gauge\nsome_other_metric {}".format(value1, value2)

if __name__ == '__main__':
    api.run(host="0.0.0.0")
