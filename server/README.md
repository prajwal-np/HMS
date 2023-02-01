<h5>Migration commit<h5>

```python 
python3 -m alembic.config revision --autogenerate -m "Added account table"
```

<h5> Migration  head</h5>
`python3 -m alembic.config upgrade head`

```sh

```

```sh

```

#Run Uvicorn
`uvicorn app.main:app --reload`
