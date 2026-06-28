{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNYd+M7qvoowtv3VQZ3NKnY"
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
        "dna = \"ATGCGTACGTTAGCTAGCTAGCT\"\n",
        "\n",
        "total_length = len(dna)\n",
        "g_count = dna.count(\"G\")\n",
        "c_count = dna.count(\"C\")\n",
        "\n",
        "combined_gc_count = g_count + c_count\n",
        "\n",
        "percentage_gc_combined = (combined_gc_count/total_length)*100\n",
        "\n",
        "print(f\"C and G combined: {percentage_gc_combined:.2f}%\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2He7Y4jl9U4s",
        "outputId": "f78b538c-0d93-4245-f4b3-871d0161ffef"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "C and G combined: 47.83%\n"
          ]
        }
      ]
    }
  ]
}