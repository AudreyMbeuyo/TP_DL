# TP Deep Learning - Classification MNIST

## Description du projet

Ce projet implémente un réseau de neurones pour la classification des chiffres manuscrits du dataset MNIST. Il couvre l'ensemble du cycle de vie d'un modèle de Deep Learning, de la conception au déploiement.

## Objectifs

- Construire et entraîner un réseau de neurones avec TensorFlow/Keras
- Utiliser MLflow pour le suivi des expérimentations
- Créer une API REST avec Flask pour servir le modèle
- Conteneuriser l'application avec Docker
- Mettre en place un workflow de versionnement avec Git

## Structure du projet

```
TP1_DL/
├── train_model.py          # Script d'entraînement du modèle
├── app.py                  # API Flask pour les prédictions
├── requirements.txt        # Dépendances Python
├── Dockerfile             # Configuration Docker
├── mnist_model.h5         # Modèle entraîné (généré)
└── README.md              # Documentation du projet
```

## Installation et configuration

### Prérequis

- Python 3.8+
- pip
- Git
- Docker 

### Installation des dépendances

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Linux/Mac :
source venv/bin/activate
# Sur Windows :
# venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

### 1. Entraînement du modèle

```bash
python train_model.py
```

Ce script :
- Charge le dataset MNIST
- Entraîne un réseau de neurones fully-connected
- Sauvegarde le modèle entraîné
- Enregistre les métriques avec MLflow

### 2. Lancement de l'interface MLflow

```bash
mlflow ui
```

Puis ouvrir http://localhost:5000 pour visualiser les expérimentations.

### 3. API de prédiction

```bash
python app.py
```

L'API sera disponible sur http://localhost:5000/predict

### 4. Test de l'API

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"image": [0, 0, 0, ..., 0]}'  # 784 valeurs entre 0 et 1
```

## Architecture du modèle

- **Couche d'entrée** : 784 neurones (images 28x28 aplaties)
- **Couche cachée** : 512 neurones avec activation ReLU
- **Dropout** : 0.2 pour éviter le surapprentissage
- **Couche de sortie** : 10 neurones avec activation softmax (classification)

## Métriques de performance

- **Précision sur les données de test** : ~97.9%
- **Temps d'entraînement** : ~5 époques
- **Optimiseur** : Adam
- **Fonction de perte** : Sparse categorical crossentropy

## Conteneurisation

### Construction de l'image Docker

```bash
docker build -t mnist-api .
```

### Lancement du conteneur

```bash
docker run -p 5000:5000 mnist-api
```

## Technologies utilisées

- **TensorFlow/Keras** : Framework de Deep Learning
- **MLflow** : Suivi des expérimentations
- **Flask** : API REST
- **Docker** : Conteneurisation
- **NumPy** : Calculs numériques
