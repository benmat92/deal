import React from 'react';
import { Container, Typography, Link, Box } from '@mui/material';

function Footer() {
  const footerStyles = {
    position: 'absolute',
    width: '100%',
    bottom: 0,
    backgroundColor: '#2c3e50',
    color: '#ecf0f1',
    padding: '20px 0',
  };

  return (
    <Box style={footerStyles}>
      <Container>
        <Typography variant="body1" align="center" gutterBottom>
          © 2023 DealFinder
        </Typography>
        <Typography variant="body2" align="center">
          <Link href="#" color="inherit" style={{ marginRight: '16px' }}>
            About
          </Link>
          <Link href="#" color="inherit" style={{ marginRight: '16px' }}>
            Privacy Policy
          </Link>
          <Link href="#" color="inherit" style={{ marginRight: '16px' }}>
            Contact
          </Link>
        </Typography>
      </Container>
    </Box>
  );
}

export default Footer;
