.PHONY: generate
generate:
	poetry run python -m grpc_tools.protoc --python_betterproto2_out=src/magic_flow_python/proto -I ./proto ./proto/flow/**/*.proto
