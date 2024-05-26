from statsmodels.tsa.holtwinters import ExponentialSmoothing

def forecast_data(data, periods=5):
    if len(data) == 0:
        return []
    model = ExponentialSmoothing(data, trend='add', seasonal=None, seasonal_periods=None)
    fit = model.fit()
    forecast = fit.forecast(periods)
    return forecast
