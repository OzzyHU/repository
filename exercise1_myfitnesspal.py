{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You have eaten a total of 2 snickers!\n"
     ]
    }
   ],
   "source": [
    "# Nutritional values snickers\n",
    "calories = 22.0\n",
    "fat = 10.0\n",
    "carbohydrate = 1.10\n",
    "protein = 4.5\n",
    "\n",
    "# Input amount of eaten snickers by the user\n",
    "amount_snickers = input(\"How many snickers have you eaten? \")\n",
    "\n",
    "# Output amount of eaten snickers by the user\n",
    "print(\"You have eaten a total of \" + amount_snickers + \" snickers!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Formula nutritions and amount snickers\n",
    "amount_snickers = int(amount_snickers)\n",
    "input_calories = amount_snickers * calories\n",
    "input_fat = amount_snickers * fat\n",
    "input_carbohydrate = amount_snickers * carbohydrate\n",
    "input_protein = amount_snickers * protein"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You have consumed a total of 44.0 calories\n",
      "You have consumed a total of 20.0 fat\n",
      "You have consumed a total of 2.2 carbohydrate\n",
      "You have consumed a total of 9.0 protein\n"
     ]
    }
   ],
   "source": [
    "# Print the total amount of nutritions per eaten snicker\n",
    "print(\"You have consumed a total of \" + str(input_calories) + \" calories\")\n",
    "print(\"You have consumed a total of \" + str(input_fat) + \" fat\")\n",
    "print(\"You have consumed a total of \" + str(input_carbohydrate) + \" carbohydrate\")\n",
    "print(\"You have consumed a total of \" + str(input_protein) + \" protein\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
