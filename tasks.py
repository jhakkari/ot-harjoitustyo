from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def built(ctx):
    ctx.run("python3 src/built.py")

@task
def test(ctx):
    ctx.run("pytest src", pty=True)
