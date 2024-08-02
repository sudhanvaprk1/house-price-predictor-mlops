from feature_engineering import engineer_features
from hyperparameter_tuning import create_objective
import mlflow 
import mlflow.sklearn
import optuna 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_model(experiment_name = "house-price-predictor",
                model_name = "RandomForestHousePricePredictor"):
    """
    Trains Random Forest Regressor for House Price Prediction dataset by tuning hyperparameters using
    Optuna.
    """
    # Import split datasets
    X_train, X_test, y_train, y_test = engineer_features()

    # Tuning hyperparameters
    objective = create_objective(X_train, y_train)
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=20)
    print('Best trial: score {}, params {}'.format(study.best_trial.value, study.best_trial.params))

    # Use the best hyperparameters to train the final model
    best_params = study.best_trial.params
    mlflow.set_experiment(experiment_name)
    with mlflow.start_run() as run:
        # Defining Random Forest Regressor with best hyperparameters
        rf = RandomForestRegressor(
            n_estimators=best_params['n_estimators'], 
            max_depth=best_params['max_depth'], 
            min_samples_split=best_params['min_samples_split'], 
            min_samples_leaf=best_params['min_samples_leaf'], 
            random_state=42
        )

        # Fitting the model 
        rf.fit(X_train, y_train)

        # Making predictions
        y_pred_rf = rf.predict(X_test)

        # Log metrics
        mse_rf = mean_squared_error(y_test, y_pred_rf)
        r2_rf = r2_score(y_test, y_pred_rf)
        mlflow.log_metric('mse', mse_rf)
        mlflow.log_metric('r2', r2_rf)

        # Log model
        mlflow.sklearn.log_model(rf, 'random_forest_model')

        print(f'Logged metrics: MSE={mse_rf}, R2={r2_rf}')
        print(f'Model saved in run {mlflow.active_run().info.run_uuid}')

        # Register the model
        model_uri = f"runs:/{run.info.run_id}/random_forest_model"
        registered_model = mlflow.register_model(model_uri=model_uri, name=model_name)
        print(f"Model registered with name: {registered_model.name} and version: {registered_model.version}")
