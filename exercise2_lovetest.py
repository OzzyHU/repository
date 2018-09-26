{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "# variable names\n",
    "name1 = input(\"First name \")\n",
    "name2 = input(\"Second name \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your name combinations are oswaldo & niek\n"
     ]
    }
   ],
   "source": [
    "# variable names\n",
    "combination_name = name1 + \" \" + \"&\" + \" \" + name2\n",
    "\n",
    "# ssignment string method \n",
    "combination_name = combination_name.lower()\n",
    "\n",
    "# assignment string method \n",
    "combination_name = combination_name.strip()\n",
    "\n",
    "print(\"Your name combinations are \" + combination_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "OSWALDO is greater than NIEK\n"
     ]
    }
   ],
   "source": [
    "# name combinations statements\n",
    "if name1 == name2: \n",
    "    print(name1 + \" \" + \"&\" + \" \" + name2 + \"are match!\")\n",
    "elif name1 > name2:\n",
    "    print(name1 + \" is greater than \" + name2)\n",
    "elif name1 < name2:\n",
    "    print(name1 + \" is lesser than \" + name2)\n",
    "else:\n",
    "    print(\"Your names are not a match. Try another combination\")"
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
