# Object Relations Lab

Welcome to Silicon Valley! For this assignment, our domain is the startup world! We have three models - `Startup`, `VentureCapitalist`, and `FundingRound`. A `Startup` has many `VentureCapitalist`s through `FundingRound`s.

## Setup

`pipenv install` will make sure we have ipdb included in our environment.  
`pipenv shell` allows us access to that environment.

## Topics

- Classes vs Instances
- Variable Scope ( Class, Instance, Local )
- Object Relationships
- Instance Methods
- Class Methods

## Notes

Your goal is to build out all of the functionality listed in the deliverables.

We've provided you with a console that you can use to test your code. To enter a console session, run `python debug.py` from the command line. You'll be able to test out the methods that you write here. Take a look at that file to see how you can pre-define variables and create object instances, rather than manually doing it in every single console session.

**Remember!** This is an exercise without tests. You cannot run `pytest`. You'll need to create your own sample instances for testing purposes. Make sure your associations and methods work in the console before submitting.

## A note about notation

When you see a '`#`', this means the functionality will be related to the instance, a '`.`', the class.

## Deliverables

### Basic Class Methods, Attributes, and Properties

#### Build the following on the `Startup` class

- `Startup#name`
  - returns a **string** that is the startup's name
- `Startup#founder`
  - returns a **string** that is the founder's name
  - Once a startup is created, the founder cannot be changed.
- `Startup#domain`
  - returns a **string** that is the startup's domain
  - Once a startup is created, the domain cannot be changed (ie. A developer working with instances of the Startup class cannot directly change the domain)
- `Startup#pivot`
  - given a string of a **domain** and a string of a **name**, change the domain and name of the startup. This is the only public method through which the domain can be changed.
- `Startup.all`
  - should return a list of **all** of the startup instances
- `Startup.find_by_founder`
  - given a string of a **founder's name**, returns the **first startup instance** whose founder's name matches
- `Startup.domains`
  - should return an **list** of all of the different startup domains

---

#### Build out the following on the `VentureCapitalist` class

- `VentureCapitalist#name`
  - returns a **string** that is the venture capitalist's name
- `VentureCapitalist#total_worth`
  - returns a **number** that is the total worth of this investor (e.g., think of it as how much money they have)
- `VentureCapitalist.all`
  - returns an list of all venture capitalist instances
- `VentureCapitalist.tres_commas_club`
  - returns an list of all venture capitalist instances in the Trés Commas club (they have more then 1,000,000,000 `total_worth`)

---

#### Build out the following on the `FundingRound` class

- `FundingRound#startup`
  - returns the startup object for that given funding round
  - Once a funding round is created, I should not be able to change the startup
- `FundingRound#venture_capitalist`
  - returns the venture capitalist object for that given funding round
  - Once a funding round is created, I should not be able to change the venture capitalist
- `FundingRound#type`
  - returns a **string** that is the type of funding round
  - Examples include: Angel, Pre-Seed, Seed, Series A, Series B, Series C, etc.
- `FundingRound#investment`
  - returns a **number** that is the amount invested during this funding round
  - This should be a float that is not a negative number.
- `FundingRound.all`
  - returns a list of all of the funding round instances.

---

### Associations and Aggregate Methods

#### Startup

- `Startup#sign_contract`
  - given a **venture capitalist object**, type of investment (as a string), and the amount invested (as a float), creates a new funding round and associates it with that startup and venture capitalist.
- `Startup#num_funding_rounds`
  - Returns the total number of funding rounds that the startup has gotten
- `Startup#total_funds`
  - Returns the total sum of investments that the startup has gotten
- `Startup#investors`
  - Returns a **unique** list of all the venture capitalists that have invested in this company
- `Startup#big_investors`
  - Returns a **unique** list of all the venture capitalists that have invested in this company and are in the Trés Commas club

#### VentureCapitalist

- `VentureCapitalist#offer_contract`
  - given a **startup object**, type of investment (as a string), and the amount invested (as a float), creates a new funding round and associates it with that startup and venture capitalist.
- `VentureCapitalist#funding_rounds`
  - returns an list of all funding rounds for that venture capitalist
- `VentureCapitalist#portfolio`
  - Returns a **unique** list of all startups this venture capitalist has funded
- `VentureCapitalist#biggest_investment`
  - returns the largest funding round given by this venture capitalist
- `VentureCapitalist#invested`
  - given a **domain string**, returns the total amount invested in that domain

---
