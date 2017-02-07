""" small town 1000 pop at 1/1   "In a small town the population is 1000 at the beginning of a year. \n",
    "\n",
    "The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. \n",
    "\n",
    "How many years does the town need to see its population greater or equal to 1200 inhabitants?\n",
    "\n",
    "Write a function to determine the the answer given input of the starting population, the number of additional inhabitants coming each year, the anual percent of increase, and the target population.\n",
    "\n",
    "solve(start_pop, additional, delta, target)\n",
    "\n",
    "```\n",
    "In: solve(1000, 50, 2, 1200)\n",
    "Out: 3 Years.\n",
    "```\n",
    "\n"
    """

def pop_sim(pop, people_in, rate, stop_pop):
    year = 2017
    new_year = year
    percentage = rate/100
    while pop < stop_pop:
        pop = pop + (pop * percentage + people_in)
        new_year += 1
        print(pop, new_year - year)

pop_sim(1000, 50, 2, 1200)
