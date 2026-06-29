{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNUHQiH8MbVO5c20ItySPod",
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
        "<a href=\"https://colab.research.google.com/github/arcPrayagscibio/learning-biotechnology-/blob/main/dna_translator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dna = \"ATGCGTACGTTAGCTAGCTAGCTATGCGTACGTTAGCTAGCTAGCT\"\n",
        "#create a translation table to map each base to its complement\n",
        "translation_table = str.maketrans(\"ATGC\",\"TAGC\")\n",
        "#apply the translation to get the complimentary strand\n",
        "dna = dna.translate(translation_table)\n",
        "print(\"the complimentary strand for this dna is\",dna)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Mxioj8LkhCqH",
        "outputId": "3092ae82-b795-43f8-f479-2ac50b831dd5"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the complimentary strand for this dna is TAGCGATCGAATGCATGCATGCATAGCGATCGAATGCATGCATGCA\n"
          ]
        }
      ]
    }
  ]
}