{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMQ2QDkGPIeuXH9lbFpCMp8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/arcPrayagscibio/learning-biotechnology-/blob/main/rna_transcriber.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dna = \"ATGCGTACGTTAGCTAGCTAGCT\"\n",
        "rna = dna.replace(\"T\",\"U\")\n",
        "print(\"the RNA sequence of this DNA is\",rna)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IEN3mwBWAhJ3",
        "outputId": "a2aa8bd4-a641-478a-9ed3-ccc4a3e1f7e9"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the RNA sequence of this DNA is AUGCGUACGUUAGCUAGCUAGCU\n"
          ]
        }
      ]
    }
  ]
}