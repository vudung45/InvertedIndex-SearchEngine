# InvertedIndex-VectorSpace
 Simple Search Engine implementing Vector Space Retrieval model


# Test
```python
print("-- Test 1 ---\nDoc1: this is test number one\nDoc2: this is test number two")
documents  = [Document("Doc1", ["this", "is", "test", "number", "one"]), Document("Doc2", ["this", "is", "test", "number", "two"])]
index = InvertedIndex(documents)
print(f'Testing with query: number one. Rankings: {index.retrieve(["number", "one"])}')
print(f'Testing with query: number one. Rankings: {index.retrieve(["number", "two"])}')
```

# Demo
 Demo from a movie search project I'm working on
```console
foo@bar:~$ python3 search_microservice/moviesearch.py

Search results for query Scarlett Johansson: [(1.0, 'Captain America 3: Civil War (2016)')]
Search results for query Thanos: [(1.0, 'Avengers: Infinity War Part I (2018)'), (1.0, 'Avengers: Endgame (2019)'), (1.0, 'Avengers 3: Infinity War (2018)'), (1.0, 'Avengers: Infinity War (2018)'), (1.0, 'Guardians Of The Galaxy (2014)')]
Search results for query Peter Quill: [(1.0, 'Guardians Of The Galaxy (2014)')]
Search results for query Groot: [(1.0, 'Guardians Of The Galaxy (2014)')]
Search results for query Peter Parker: [(1.0, 'Venom (2018)'), (1.0, 'Spider Man 2 (2004)'), (1.0, 'Spider Man 3 (2007)'), (1.0, 'Spider-man: Far From Home (2019)')]
Search results for query nghiện ngập: [(1.0, 'Enter the Void (2009)'), (1.0, 'Hesher (2015)'), (1.0, 'An Act Of War (2015)'), (1.0, 'Me And You (2012)'), (1.0, 'Elementary Season 5 (2016)'), (1.0, 'BloodFather (2016)'), (1.0, 'Horrible Bosses 2 (2014)'), (1.0, 'Burnt (2015)'), (1.0, 'Elementary (Season 1) (2012)'), (1.0, 'Beautiful Boy (2018)')]
Search results for query siêu anh hùng: [(1.0000000000000002, 'American Hero (2015)'), (1.0000000000000002, 'The Avengers (2012)'), (1.0000000000000002, 'Kick-Ass (2010)'), (1.0000000000000002, 'The Other Guys (2010)'), (1.0000000000000002, 'Sleight (2016)'), (1.0000000000000002, 'Justice League: War (2014)'), (1.0000000000000002, 'Captain America 2: The Winter Soldier (2014)'), (1.0000000000000002, 'Thor: The Dark World (2013)'), (1.0000000000000002, 'Doctor Strange (2016)'), (1.0000000000000002, 'X-Men Origins: Wolverine (2009)')]
```
