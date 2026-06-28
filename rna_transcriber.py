{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMGaFQyBbKKICLccWJ73OHW"
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
      "cell_type": "code",
      "source": [
        "from typing import Sequence\n",
        "dna = \"ATGCGTACGTTAGCTAGCTAGCT\"\n",
        "print (\"length of this dna Sequence is.\",len(dna))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Tqp8r8U0FJ4X",
        "outputId": "71f92e92-0efb-4df0-e22f-46a2fa14134c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "length of this dna Sequence is. 23\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dna = \"ATGCGTACGTTAGCTAGCTAGCT\"\n",
        "dna = dna.replace(\"T\",\"U\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "ZLZCvhvJ4GqB",
        "outputId": "d3cfc4c3-73a2-4d04-eb18-40085c144c19"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndentationError",
          "evalue": "unexpected indent (3975738802.py, line 2)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_2261/3975738802.py\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    \"ATGCGTACGTTAGCTAGCTAGCT\" = \"ATGCGTACGTTAGCTAGCTAGCT\".replace(\"T\",\"U\")\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dna = \"ATGCGTACGTTAGCTAGCTAGCT\"\n",
        "dna = dna.replace(\"T\",\"U\")\n",
        "print(\"The replaced DNA sequence is:\", dna)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "6caoEfOd4xZd",
        "outputId": "284a2ed5-8b96-4b98-cae5-08183f536ba8"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax. Perhaps you forgot a comma? (477499408.py, line 3)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_2261/477499408.py\"\u001b[0;36m, line \u001b[0;32m3\u001b[0m\n\u001b[0;31m    print(\"print the replaced dna sequence.replace(\"T\",\"U\")\")\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dna = \"ATGCGTACGTTAGCTAGCTAGCT\"\n",
        "rna = dna.replace(\"T\",\"U\")\n",
        "print(\"the replaced RNA sequence is:\",rna)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KF7EcFhi5jEN",
        "outputId": "cd652bcb-1ad7-4ff2-db1e-24b9d942662f"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the replaced RNA sequence is: AUGCGUACGUUAGCUAGCUAGCU\n"
          ]
        }
      ]
    }
  ]
}