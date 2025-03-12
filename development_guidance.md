# Development Guidance

## Sourcegraph Code Graph Property
- Install the Sourcegraph VS Code extension.
- Configure your repository with Sourcegraph to enable advanced code navigation and insights.
- Regularly update the extension and review its configuration to leverage new features.

## Model Context Protocol (MCP) Servers Management
- Document the configuration details of all integrated MCP servers.
- Ensure environment variables for MCP servers are correctly set in your .env configuration.
- Consider containerization of MCP servers to improve scalability and manageability.

## Version Conflict Identification
- Periodically run dependency audits using tools like pipdeptree to visualize dependency trees.
- Review version constraints in pyproject.toml to detect potential conflicts.
- Update dependencies cautiously after confirming compatibility.

## Containerization Options
- Use Docker to containerize your development services, including PostgreSQL, Redis, and MCP servers.
- Create Dockerfiles and Docker Compose configurations to orchestrate multi-container deployments.
- Containerization helps in ensuring environment consistency across different stages.

## Recommended VS Code Extensions
- Python, Django, and Pylance for enhanced language support.
- Docker and Remote Development extensions for streamlined container management.
- GitLens for improved Git integration and code insight.
- Sourcegraph for advanced code navigation within your repository.

## Environment Variables Setup
- Confirm that all environment variables defined in .env.example are set appropriately.
- Use secure methods to manage API keys and sensitive configuration data.

## macOS Performance Optimizations
- Utilize native monitoring tools like Activity Monitor to track system resources.
- Regularly update macOS to the latest stable version for performance improvements.
- Optimize resource allocation and consider using lightweight window managers if system performance is critical.

## Next Steps
- Continuously update documentation to reflect configuration and environment changes.
- Integrate CI/CD pipelines to detect conflicts and performance issues early.
- Review and update configuration settings as new tools and technology updates become available.