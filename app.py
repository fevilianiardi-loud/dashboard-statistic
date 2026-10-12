from flask import Flask, render_template
import csv
import statistics

app = Flask(__name__)

def load_data():
    with open("data.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def descriptive(values):
    values = [float(v) for v in values]
    return {
        "count": len(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "min": min(values),
        "max": max(values),
        "range": max(values) - min(values),
        "stdev": statistics.stdev(values) if len(values) > 1 else 0
    }

@app.route("/")
def dashboard():
    data = load_data()
    x_stats = descriptive([row["X"] for row in data])
    y_stats = descriptive([row["Y"] for row in data])

    # Korelasi Pearson untuk membantu analisis pola X dan Y.
    xs = [float(row["X"]) for row in data]
    ys = [float(row["Y"]) for row in data]
    x_mean = statistics.mean(xs)
    y_mean = statistics.mean(ys)
    numerator = sum((a-x_mean)*(b-y_mean) for a,b in zip(xs,ys))
    denominator = (
        sum((a-x_mean)**2 for a in xs) *
        sum((b-y_mean)**2 for b in ys)
    ) ** 0.5
    correlation = numerator / denominator if denominator else 0

    return render_template(
        "index.html",
        data=data,
        x=x_stats,
        y=y_stats,
        correlation=correlation
    )

if __name__ == "__main__":
    app.run(debug=True)
