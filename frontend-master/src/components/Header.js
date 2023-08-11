import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import CssBaseline from '@mui/material/CssBaseline';
import { styled } from '@mui/material/styles';
import { NavLink } from 'react-router-dom';
import Link from '@mui/material/Link';
import Button from '@mui/material/Button';

// For an active link styling with react-router's NavLink
const StyledNavLink = styled(NavLink)({
    textDecoration: 'none',
    color: 'inherit',
    '&.active': {
        textDecoration: 'underline',
    },
});

function Header() {
    return (
        <>
            <CssBaseline />
            <AppBar position="static" color="default" elevation={0}>
                <Toolbar>
                    <Typography variant="h6" color="inherit" noWrap>
                        DealHunt
                    </Typography>
                    <nav>
                        <Link variant="button" color="textPrimary" component={StyledNavLink} to="/login" style={{ marginLeft: 15 }}>
                            Login
                        </Link>
                        <Link variant="button" color="textPrimary" component={StyledNavLink} to="/register" style={{ marginLeft: 15 }}>
                            Register
                        </Link>
                    </nav>
                    <Button color="primary" variant="outlined" style={{ marginLeft: 'auto' }}>
                        Logout
                    </Button>
                </Toolbar>
            </AppBar>
        </>
    );
}

export default Header;
