#include "app/SQL.h"

#include "app/Error.h"

#include "jdbc/cppconn/connection.h"
#include "jdbc/cppconn/prepared_statement.h"
#include "jdbc/mysql_driver.h"

namespace app {

SQL::SQL(std::string_view preparedStatement)
{
    LoadStatement(preparedStatement);
}

SQL::~SQL()
{
    if (m_Statement)
        delete m_Statement;
    if (m_Connection)
        delete m_Connection;

    m_Statement  = nullptr;
    m_Connection = nullptr;
}

void SQL::LoadStatement(std::string_view preparedStatement)
{
    try
    {
        sql::mysql::MySQL_Driver* driver = sql::mysql::get_mysql_driver_instance();
        m_Connection                     = driver->connect("tcp://127.0.0.1:3306", "root", "");
        m_Connection->setSchema("archer_database");

        m_Statement = m_Connection->prepareStatement(preparedStatement.data());

    } catch (sql::SQLException& e)
    {
        FATAL("Database Error: {}", e.what());
    }
}

void SQL::Bind(std::string_view str)
{
    try
    {
        m_Statement->setString(m_BindIndex, str.data());
        m_BindIndex++;

    } catch (sql::SQLException& e)
    {
        ERROR("Database Error: {}", e.what());
    }
}

void SQL::Bind(unsigned int val)
{
    try
    {
        m_Statement->setInt(m_BindIndex, val);
        m_BindIndex++;

    } catch (sql::SQLException& e)
    {
        ERROR("Database Error: {}", e.what());
    }
}

UpdateSQL::UpdateSQL(std::string_view preparedStatement)
    : SQL(preparedStatement)
{
}

bool UpdateSQL::Execute()
{
    try
    {
        m_Statement->executeUpdate();
        return true;

    } catch (sql::SQLException& e)
    {
        ERROR("Database Error: {}", e.what());
        return false;
    }
}

SelectSQL::SelectSQL(std::string_view preparedStatement)
    : SQL(preparedStatement),
      m_Results(nullptr)
{
}

SelectSQL::~SelectSQL()
{
    if (m_Results)
        delete m_Results;
    m_Results = nullptr;
}

bool SelectSQL::Execute()
{
    try
    {
        m_Results = m_Statement->executeQuery();
        return true;

    } catch (sql::SQLException& e)
    {
        ERROR("Database Error: {}", e.what());
        return false;
    }
}

} // namespace app
