from app.coderunner.repl import CodeExecutor
from timeit import default_timer as timer


async def execute_code(code: str) -> str:
    code = code.strip().strip("\n")

    try:
        executor = CodeExecutor()
        start = timer()
        output = executor.execute_python(code)
        end = timer()
    except Exception as e:
        raise Exception(e)

    result = f"Result \n{output}Execution time: {end-start:.3f}s"
    
    return result