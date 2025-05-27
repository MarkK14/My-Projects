#include <initializer_list>
#include <iostream>
#include <cassert>

/// Set class declaration ///////////////////////////////////////////////////////////////////////////////////

class Set{

public:
  Set(std::initializer_list<int> initial_values);
  ~Set();
  Set(Set const &orig);
  Set(Set &&orig);
  Set &operator=(Set const &orig);
  Set &operator=(Set &&orig);
  bool empty() const;
  std::size_t size() const;
  void clear();
  Node *find(int const &item) const;
  std::size_t insert(int const &item);
  std::size_t insert(int const array[], std::size_t const begin, std::size_t const end);
  std::size_t erase(int const &item);
  std::size_t merge(Set &other);
  Set &operator|=(Set const &other);
  Set &operator&=(Set const &other);
  Set &operator^=(Set const &other);
  Set &operator-=(Set const &other);
  Set operator|(Set const &other) const;
  Set operator&(Set const &other) const;
  Set operator^(Set const &other) const;
  Set operator-(Set const &other) const;
  bool operator<=(Set const &other) const;
  bool operator>=(Set const &other) const;
  bool operator<(Set const &other) const;
  bool operator>(Set const &other) const;
  bool operator==(Set const &other) const;
  bool operator!=(Set const &other) const;

private:
  Node *p_head_;
  friend std::ostream &operator<<(std::ostream &out, Set const &rhs);
};


/// Node class declaration  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Node
{
public:
  Node(int new_value, Node *new_next);
  int value() const;
  Node *next() const;

private:
  int value_;
  Node *next_;

  friend class Set;
};


/// Node class Definition   //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// Node constructor
Node::Node(int new_value, Node *new_next) : value_{new_value},next_{new_next} {

}

int Node::value() const
{
  return value_;
}

Node* Node::next() const
{
  return next_;
}


///Set class definition/////////////////////////////////////////////////////////////////

// Initializing constructor
Set::Set(std::initializer_list<int> initial_values) : p_head_{nullptr}
{
  for (int const &value : initial_values)
  {
    insert(value);
  }
}

// Destructor
Set::~Set()
{
  clear();
}

// Copy constructor
Set::Set(Set const &orig) : p_head_{nullptr}
{
  for (Node *ptr{orig.p_head_};ptr != nullptr; ptr = ptr->next()){
    insert(ptr->value());
  }
}

// Move constructor
Set::Set(Set &&orig) : p_head_{nullptr}
{
  std::swap(p_head_, orig.p_head_);
}

// Copy assignment
Set &Set::operator=(Set const &orig)
{
  if (this == &orig)
  {
    return *this;
  }

  clear();
  for (Node *x = orig.p_head_; x != nullptr; x = x->next()) // Use next(), not next_
  {
    insert(x->value());
  }
  return *this;
}

// Move assignment
Set &Set::operator=(Set &&orig)
{
  if (this != &orig)
  {
    std::swap(p_head_, orig.p_head_);
  }
  return *this;
}

// Empty
bool Set::empty() const
{
  if (p_head_ == nullptr)
  {
    return true;
  }
  return false;
}

// Size
size_t Set::size() const
{
  std::size_t x{0};
  for (Node *ptr{p_head_};ptr != nullptr; ptr = ptr->next())
  {
    x++;
  }
  return x;
}

// Clear
void Set::clear()
{
  Node *ptr = p_head_;
  while (ptr != nullptr)
  {
    Node *tmp = ptr->next();
    delete ptr;
    ptr = tmp;
  }
  p_head_ = nullptr;
}
// Find
Node *Set::find(int const &item) const
{

  for (Node *ptr{
           p_head_};
       ptr != nullptr; ptr = ptr->next())
  {
    if (ptr->value_ == item)
    {
      return ptr;
    }
  }

  return nullptr;
}

// Insert the item into the set
std::size_t Set::insert(int const &item)
{
  if (this->find(item) == nullptr)
  {
    Node *ptr_item = new Node(item, nullptr);

    if (p_head_ == nullptr)
    {
      p_head_ = ptr_item;
    }
    else
    {
      ptr_item->next_ = p_head_;
      p_head_ = ptr_item;
    }

    return 1;
  }

  return 0;
}

// Insert all the items in the array
std::size_t Set::insert(int const array[], std::size_t const begin, std::size_t const end)
{
  std::size_t counter{0};
  for (std::size_t x{ begin};x < end; x++)
  {
    counter += insert(array[x]);
  }
  return counter;
}

// Remove the item from the set and
// return the number of items removed.
std::size_t Set::erase(int const &item)
{
  Node *prev = nullptr;
  Node *current = p_head_;

  while (current != nullptr)
  {
    if (current->value() == item)
    {
      if (prev == nullptr)
      {
        p_head_ = current->next();
      }
      else
      {
        prev->next_ = current->next();
      }
      delete current;
      return 1;
    }
    prev = current;
    current = current->next();
  }

  return 0;
}

// Move any items from 'other', whose values
// do not appear in 'this', to 'this'.
// Leave any items that already appear
// in both sets, in both sets.
std::size_t Set::merge(Set &other)
{
  std::size_t count{0};
  Node *prev = nullptr;
  Node *current = other.p_head_;

  while (current != nullptr)
  {
    if (this->find(current->value()) == nullptr)
    {
      if (prev == nullptr)
      {
        other.p_head_ = current->next();
      }
      else
      {
        prev->next_ = current->next();
      }
      insert(current->value());
      current = current->next();
      count++;
    }
    else
    {
      prev = current;
      current = current->next();
    }
  }

  return count;
}

//////////////////////
/// Set operations ///
//////////////////////
Set &Set::operator|=(Set const &other)
{
  Node *current = other.p_head_;
  while (current != 0)
  {
    if (find(current->value()) == nullptr)
    {
      this->insert(current->value());
    }
    current = current->next();
  }
  return *this;
}

Set &Set::operator&=(Set const &other)
{
  Node *current = p_head_;
  while (current != nullptr)
  {
    Node *next = current->next();
    if (other.find(current->value()) == nullptr)
    {
      this->erase(current->value());
    }
    current = next;
  }
  return *this;
}

Set &Set::operator^=(Set const &other)
{
  for (Node *ptr = other.p_head_; ptr != nullptr; ptr = ptr->next())
  {
    if (find(ptr->value()) != nullptr)
    {
      erase(ptr->value());
    }
    else
    {
      insert(ptr->value());
    }
  }
  return * this;
}

Set &Set::operator-=(Set const &other)
{
  Node *current = p_head_;
  while (current != nullptr)
  {
    Node *next = current->next();
    if (other.find(current->value()) != nullptr)
    {
      this->erase(current->value());
    }
    current = next;
  }
  return *this;
}

Set Set::operator|(Set const &other) const
{
  Set result{};
  result = *this;
  result |= other;
  return result;
}

Set Set::operator&(Set const &other) const
{
  Set result{};
  result = *this;
  result &= other;
  return result;
}

Set Set::operator^(Set const &other) const
{
  Set result{};
  Node *current = p_head_;
  while (current != nullptr)
  {
    if (other.find(current->value()) == nullptr)
    {
      result.insert(current->value());
    }
    current = current->next();
  }

  current = other.p_head_;
  while (current != nullptr)
  {
    if (find(current->value()) == nullptr)
    {
      result.insert(current->value());
    }
    current = current->next();
  }

  return result;
}

Set Set::operator-(Set const &other) const
{
  Set result{};
  result = *this;
  result -= other;
  return result;
}

// Returns 'true' if the 'other' set
// is a subset of 'this' set; that is,
// all entries in the 'other' set are
// also in this set.
bool Set::operator>=(Set const &other) const
{
  Node *current = other.p_head_;
  while (current != nullptr)
  {
    if (this->find(current->value()) == nullptr)
    {
      return false;
    }
    current = current->next();
  }
  return true;
}

bool Set::operator<=(Set const &other) const
{
  Node *current = p_head_;
  while (current != nullptr)
  {
    if (other.find(current->value()) == nullptr)
    {
      return false;
    }
    current = current->next();
  }
  return true;
}

bool Set::operator>(Set const &other) const
{
  if (size() <= other.size())
  {
    return false;
  }

  Node *current = other.p_head_;
  while (current != nullptr)
  {
    if (find(current->value()) == nullptr)
    {
      return false;
    }
    current = current->next();
  }

  return true;
}

bool Set::operator<(Set const &other) const
{
  if (size() >= other.size())
  {
    return false;
  }

  Node *current = p_head_;
  while (current != nullptr)
  {
    if (other.find(current->value()) == nullptr)
    {
      return false;
    }
    current = current->next();
  }

  return true;
}

bool Set::operator==(Set const &other) const
{
  if (size() != other.size())
  {
    return false;
  }

  Node *current = other.p_head_;
  while (current != nullptr)
  {
    if (find(current->value()) == nullptr)
    {
      return false;
    }
    current = current->next();
  }
  return true;
}

bool Set::operator!=(Set const &other) const
{
  if (size() != other.size())
  {
    return true;
  }
  Node *current = other.p_head_;
  while (current != nullptr)
  {
    if (find(current->value()) == nullptr)
    {
      return true;
    }
    current = current->next();
  }

  return false;
}

////////////////////////////////////////////
/// Supplied Code for print Set objects  ///
////////////////////////////////////////////
/// @brief Overloads the << operator allowing the print of Set objects
/// @param out The ostream to print to (e.g. std::cout <<)
/// @param rhs The Set to print (e.g. << set_A)
/// @note You do not need to edit or alter this code
std::ostream &operator<<(std::ostream &out, Set const &rhs)
{
  out << "{";
  if (!rhs.empty())
  {
    out << rhs.p_head_->value();
    for (Node *ptr{
             rhs.p_head_->next()};
         ptr != nullptr; ptr = ptr->next())
    {
      out << ", " << ptr->value();
    }
  }
  out << "}";

  return out;
}