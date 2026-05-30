#pragma once

#include "jdbc/cppconn/resultset.h"
#include <string_view>

namespace sql {

class Connection;
class PreparedStatement;

} // namespace sql

namespace app {

class SQL
{
public:
    SQL(std::string_view preparedStatement);
    virtual ~SQL();

    void BindString(std::string_view str);
    virtual bool Execute() = 0;

protected:
    unsigned m_BindIndex = 1;
    sql::PreparedStatement* m_Statement;
    sql::Connection* m_Connection;
};

class UpdateSQL : public SQL
{
public:
    UpdateSQL(std::string_view preparedStatement);

    bool Execute() override;
};

class SelectSQL : public SQL
{
public:
    SelectSQL(std::string_view preparedStatement);
    ~SelectSQL() override;

    bool Execute() override;
    sql::ResultSet* GetResults() { return m_Results; }

private:
    sql::ResultSet* m_Results;
};

} // namespace app
